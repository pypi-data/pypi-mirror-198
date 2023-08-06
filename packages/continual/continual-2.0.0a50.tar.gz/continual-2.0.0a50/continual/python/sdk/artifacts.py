from __future__ import annotations
from typing import List, Optional, Tuple
import os
import io
import requests
import tarfile
import pandas as pd
from PIL import Image
import mimetypes
from google.resumable_media import DataCorruption
from google.resumable_media.requests import ResumableUpload

from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.rpc.management.v1 import management_pb2, types

CHUNK_SIZE = 117440512  # 112 MB in bytes, chosen arbitrarily
MAX_TABLE_ROWS = 1000  # limit table to 1000 rows to keep managable


class ArtifactsManager(Manager):
    """Manages artifact resources."""

    # the name pattern for artifacts depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        id: str = "",
        path: str = "",
        table: pd.DataFrame = None,
        image: Image = None,
        external: bool = False,
        url: str = None,
        upload: bool = True,
        mime_type: str = None,
        tags: dict[str, str] = None,
        replace_if_exists: bool = False,
    ) -> Artifact:
        """Create artifact.

        Arguments:
            id: An id to uniquely identify the artifact for a given parent.
            path: Path to the artifact in the local filesystem if not external.
            table: A pandas Dataframe representing a table to store.
            image: An Image to store as a png.
            external: True if this artifact will be stored in a Continual google bucket, false if it is remote.
            url: URL for the artifact. Is a signed URL to a google bucket if artifact is not external,
                 optional user-provided URL if it is an external artifact.
            upload: Whether to upload the artifact specified in `path`. Only valid if external=False.
            mime_type: The mime type of the artifact. If internal artifact, provided value will be
                 overwritten by what is inferred from the file at `path`.
            tags: A dictionary of key-value pairs to associate with the artifact.
            replace_if_exists: If true, delete the current version of this artifact and create a new one with the same id.

        Returns:
            An Artifact

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> with open("test.txt", "w") as f:
            ...     f.write("test content")
            >>> dataset_version.artifacts.create(
            ...     id="test-artifact-internal",
            ...     path=os.path.join(os.getcwd(), "test.txt"),
            ...     external=False,
            ...     upload=True
            ... )
            <Artifact object {'name': 'projects/continual_test_proj...", 'external': True ...}>
            >>> dataset_version.artifacts.create(
            ...     id="test-artifact-external",
            ...     external=True,
            ...     url="http://test-url"
            ... )
            <Artifact object {'name': 'projects/continual_test_proj...", 'external': False ...}>
            >>> dataset_version.artifacts.create(
            ...     external=True,
            ...     url="http://test-url"
            ... )
            <Artifact object {'name': 'projects/continual_test_proj.../artifacts/cesceta5lsrkagaitfh0", 'external': False ...}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        if external or not upload:
            req = management_pb2.CreateArtifactRequest(
                parent=self.parent,
                artifact=Artifact(
                    path=path,
                    external=True,
                    url=url,
                    run=self.run_name,
                    tags=tags,
                    mime_type=mime_type,
                    current_run=self.run_name,
                ).to_proto(),
                artifact_id=id,
                replace_if_exists=replace_if_exists,
            )
            res = self.client._management.CreateArtifact(req)
            return Artifact.from_proto(
                res, client=self.client, current_run=self.run_name
            )

        elif upload:
            if path == "" and table is None and image is None:
                raise ValueError("Either a path, table or image must be provided")

            artifact_name = ""
            try:
                payload = ""
                mime_type = ""
                if path != "":
                    # if path is provided, upload file(s)
                    file_to_upload = path
                    if os.path.isdir(path):
                        tarfile_name = os.path.basename(path) + ".tar.gz"
                        with tarfile.open(tarfile_name, "w:gz") as tar:
                            tar.add(
                                path,
                                recursive=True,
                                arcname=os.path.basename(tarfile_name).split(".")[0],
                            )
                        file_to_upload = tarfile_name

                    mime_type, _ = mimetypes.guess_type(file_to_upload)

                    with open(file_to_upload, "rb") as f:
                        payload = f.read()
                elif table is not None:
                    # if table (dataframe) is provided, upload table data
                    # check size
                    row_count = len(table)
                    if row_count > MAX_TABLE_ROWS:
                        print(
                            f"warning: table exceeds max row count of {MAX_TABLE_ROWS}. Truncating table."
                        )
                        table = table[:MAX_TABLE_ROWS]
                    payload = table.to_json(orient="table")
                    mime_type = "application/vnd.dataresource+json"
                    path = f"{id}.json"
                elif image is not None:
                    # if image is provided, upload image data
                    b = io.BytesIO()
                    image.save(b, "PNG")
                    payload = b.getvalue()
                    mime_type = "image/png"
                    path = f"{id}.png"

                total_bytes = len(payload)
                exceeds_chunk_size = total_bytes >= CHUNK_SIZE

                req = management_pb2.GenerateArtifactUploadURLRequest(
                    parent=self.parent,
                    artifact_id=id,
                    artifact=Artifact(
                        path=path,
                        mime_type=mime_type or "",
                        run=self.run_name,
                        tags=tags,
                        external=False,
                        current_run=self.run_name,
                        size=total_bytes,
                    ).to_proto(),
                    resumable=exceeds_chunk_size,
                    replace_if_exists=replace_if_exists,
                )
                res = self.client._management.GenerateArtifactUploadURL(req)

                upload_url = res.url
                artifact_name = res.artifact.name

                headers = dict()
                if mime_type:
                    headers["Content-Type"] = mime_type

                if exceeds_chunk_size:
                    transport = requests.Session()

                    stream = io.BytesIO(payload)

                    upload = ResumableUpload(upload_url, CHUNK_SIZE)
                    upload._resumable_url = upload_url
                    upload._total_bytes = total_bytes
                    upload._stream = stream

                    while not upload.finished:
                        try:
                            print("Writing chunk ... ")
                            response = upload.transmit_next_chunk(transport, timeout=60)
                            print(f"Chunk response: {response}")
                        except DataCorruption:
                            raise
                else:
                    upload_res = requests.put(
                        upload_url, data=payload, headers={"Content-Type": mime_type}
                    )
                    upload_res.raise_for_status()

                return Artifact.from_proto(
                    res.artifact, client=self.client, current_run=self.run_name
                )
            except:
                if artifact_name:
                    req = management_pb2.DeleteArtifactRequest(name=artifact_name)
                    res = self.client._management.DeleteArtifact(req)
                raise

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[Artifact]:
        """List artifacts.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list of artifacts.
            latest: If true, the results are sorted in descending order, else ascending.

        Returns:
            A list of artifacts.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test_artifact_{i}", path="example_path/test.txt") for i in range(5)]
            >>> [a.key for a in dataset_version.artifacts.list(page_size=2)]
            ['test_artifact_4', 'test_artifact_3']
            >>> [a.key for a in dataset_version.artifacts.list(page_size=2)]
            ['test_artifact_0', 'test_artifact_1']
        """
        req = management_pb2.ListArtifactsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListArtifacts(req)
        return [
            Artifact.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.artifacts
        ]

    def get(self, id: str = "") -> Artifact:
        """Get artifact.

        Arguments:
            id: A unique id for the artifact.

        Returns:
            An artifact.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(id=f"test-artifact-{i}", path="example_path/test.txt") for i in range(5)]
            >>> dataset_version.artifacts.get(id="test-artifact-0")
            <Artifact object {'name': 'projects/continual_test_proj...", 'id': 'test-artifact-0', 'external': False ...}>
        """
        if not self.client:
            print(f"Cannot fetch artifact without client")
            return

        req = management_pb2.GetArtifactRequest(
            name=self.name(id, self.parent, f"{self.parent}/artifacts/{id}")
        )
        res = self.client._management.GetArtifact(req)
        return Artifact.from_proto(res, client=self.client, current_run=self.run_name)

    def delete(self, id: str):
        """Delete artifact.

        Arguments:
            id: The id or fully qualified name of the artifact

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test-artifact-{i}", path="example_path/test.txt") for i in range(5)]
            >>> [dataset_version.artifacts.delete(a.name) for a in dataset_version.artifacts.list(page_size=5)]
            [None, None, None, None, None]
            >>> len(dataset_version.artifacts.list(page_size=5))
            0
        """
        if not self.client:
            print(f"Cannot delete artifact without client")
            return

        req = management_pb2.DeleteArtifactRequest(
            name=self.name(id, self.parent, f"{self.parent}/artifacts/{id}")
        )
        self.client._management.DeleteArtifact(req)

    def download(
        self,
        id: str,
        download_dir: str = "./artifacts",
    ) -> Tuple[Artifact, str]:
        """Download artifact.

        Arguments:
            id: The name or id of the artifact
            download_dir: The directory to which to download the artifact

        Returns:
            A tuple of the Artifact object and the path where it was downloaded.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> with open("test.txt", "w") as f:
            ...     f.write("test content")
            >>> artifact = dataset_version.artifacts.create(
            ...     key="test-artifact-internal",
            ...     path=os.path.join(os.getcwd(), "test.txt"),
            ...     external=False,
            ...     type="txt",
            ...     metadata={"key": "value"},
            ...     upload=True
            ... )
            >>> artifact, dest_path = dataset_version.artifacts.download(id=artifact.id) # Download the artifact
            >>> with open(dest_path, "r") as f:
            ...     print(f.read())
            "test content"
        """

        artifact = self.get(id)
        downloaded_to = ""
        if not artifact.url:
            raise ValueError(
                f"Artifact cannot be downloaded - no URL was found: {artifact.url}"
            )
        elif artifact.external:
            raise ValueError(f"Cannot download an external artifact - {artifact.url}")

        try:
            res = requests.get(artifact.url, stream=True)
            with tarfile.open(fileobj=res.raw, mode="r") as f:
                f.extractall(download_dir)

            root_dir = os.path.basename(artifact.path or "").split(".")[0]
            downloaded_to = os.path.join(download_dir, root_dir)
        except:
            res = requests.get(artifact.url)
            downloaded_to = os.path.join(
                download_dir,
                os.path.basename(artifact.path or artifact.name.split("/")[-1]),
            )
            with open(downloaded_to, "wb") as f:
                f.write(res.content)
        return artifact, downloaded_to

    def update(
        self,
        paths: List[str],
        artifact: Artifact,
    ) -> Artifact:
        """Update Artifact.

        Arguments:
            paths: A list of paths to be updated.
            artifact: Artifact object containing updated fields.

        Returns:
            An updated Artifact.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
        """

        req = management_pb2.UpdateArtifactRequest(
            artifact=artifact.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateArtifact(req)
        return Artifact.from_proto(resp, client=self.client, current_run=self.run_name)


class Artifact(Resource, types.Artifact):
    """Artifact resource."""

    # the name pattern for artifacts depends on the resource it was created for
    name_pattern: str = ""

    _manager: ArtifactsManager
    """Artifact manager."""

    def _init(self):
        self._manager = ArtifactsManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )

    def download(self, dest_dir: str = "./artifacts") -> Tuple[Artifact, str]:
        """Download artifact.

        Arguments:
            dest_dir: The directory to which to download the artifact

        Returns:
            A tuple of the Artifact object and the path where it was downloaded.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> with open("test.txt", "w") as f:
            ...     f.write("test content")
            >>> artifact = dataset_version.artifacts.create(
            ...     key="test-artifact-internal",
            ...     path=os.path.join(os.getcwd(), "test.txt"),
            ...     external=False,
            ...     type="txt",
            ...     metadata={"key": "value"},
            ...     upload=True
            ... )
            >>> artifact, dest_path = artifact.download() # Download the artifact
            >>> with open(dest_path, "r") as f:
            ...     print(f.read())
            "test content"
        """
        # Create if the default doesnt exist
        if dest_dir == "./artifacts":
            dest_dir = os.path.join(os.getcwd(), "artifacts")
            os.makedirs(dest_dir, exist_ok=True)
        return self._manager.download(id=self.name, download_dir=dest_dir)

    def delete(self):
        """Delete artifact.

        Examples:
            >>> ... # Assume we have an environment defined
            >>> run = env.runs.create("my-run")
            >>> dataset = run.datasets.create("test_dataset")
            >>> dataset_version = dataset.dataset_versions.create()
            >>> artifacts = [dataset_version.artifacts.create(key=f"test_artifact_{i}", path="example_path/test.txt") for i in range(5)]
            >>> [a.delete() for a in dataset_version.artifacts.list(page_size=5)]
            [None, None, None, None, None]
            >>> len(dataset_version.artifacts.list(page_size=5))
            0
        """
        self._manager.delete(name=self.name)

    def update(self, paths: List[str]) -> Artifact:
        """Update Artifact.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Artifact.

        Examples:
            >>> ...
        """
        return self._manager.update(paths=paths, artifact=self)

    def add_tags(self, tags: dict[str, str]) -> Artifact:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Artifact.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> artifact = dataset_version.artifacts.get("test-table")
            >>> artifact.add_tags({"color": "blue", "fruit": "apple"})
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(artifact=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Artifact:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Artifact.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> artifact = dataset_version.artifacts.get("test-table")
            >>> artifact.remove_tags({"color", "fruit"})
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(artifact=self, paths=["tags"])
