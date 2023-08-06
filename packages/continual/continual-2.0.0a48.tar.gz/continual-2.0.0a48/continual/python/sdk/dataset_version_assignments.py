from __future__ import annotations
from typing import List, Optional

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager


class DatasetVersionAssignmentManager(Manager):
    """Manages DatasetVersionAssignment resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/datasets/{dataset}/versions/{version}/assignments/{assignment}"

    def create(
        self,
        resource_name: str,
        id: Optional[str] = "",
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> DatasetVersionAssignment:
        """Create a dataset version assignment.

        A dataset version assignment associates a dataset version with a resource such as a model version or batch prediction.

        Argument:
            resource_name: The resource that is downstream of this parent dataset version
            id: An optional DatasetVersionAssignment id.
            tags: A dict of str: str tags to associate with the assignment.
            replace_if_exists: If True, update the assignment if it already exists.

        Returns
            A DatasetVersionAssignment.

        Examples:
            >>> ... # Assume dataset_version and model_version are defined
            >>> dataset_version.assignments.create(resource_name=model_version.name)
            <DatasetVersionAssignment object {'name': 'projects/continual_test_proj/environments/production/datasets/test_dataset/versions/cegig6q5lsrt9r5a8nl0/assignments/cegigs25lsrt9r5a8no0',
            'resource_name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cegig6q5lsrt9r5a8nmg', 'create_time': '2022-12-20T03:13:52.354991Z'}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateDatasetVersionAssignmentRequest(
            parent=self.parent,
            assignment=DatasetVersionAssignment(
                resource_name=resource_name,
                tags=tags,
                run=self.run_name,
                current_run=self.run_name,
            ).to_proto(),
            assignment_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateDatasetVersionAssignment(req)
        return DatasetVersionAssignment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def get(self, id: str) -> DatasetVersionAssignment:
        """Get a dataset version assignment.

        Arguments:
            id: DatasetVersionAssignment name or id.

        Returns:
            A DatasetVersionAssignment.

        Examples:
            >>> ... # Assume dataset_version and model_version are defined
            >>> dv_assignment = dataset_version.assignments.create(id='example-assignment', resource_name=model_version.name)
            >>> dataset_version.assignments.get("example-assignment")
            <DatasetVersionAssignment object {'name': 'projects/continual_test_proj/environments/production/datasets/test_dataset/versions/cegig6q5lsrt9r5a8nl0/assignments/example-assignment',
            'resource_name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cegig6q5lsrt9r5a8nmg', 'create_time': '2022-12-20T03:13:52.354991Z'}>
        """

        req = management_pb2.GetDatasetVersionAssignmentRequest(name=self.name(id))
        resp = self.client._management.GetDatasetVersionAssignment(req)
        return DatasetVersionAssignment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[DatasetVersionAssignment]:
        """List dataset version assignments.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            latest: If true, the results are sorted in descending order, else ascending.

        Returns:
            A list of DatasetVersionAssignments.

        Examples:
            >>> ... # Assume run is defined
            >>> dataset_version = run.datasets.create("test_dataset").dataset_versions.create()
            >>> model_versions = [
                    run.models.create(f"test_model_{i}").model_versions.create()
                    for i in range(5)
                ]
            >>> dv_assignments = [
                    dataset_version.assignments.create(resource_name=mv.name)
                    for mv in model_versions
                ]
            >>> len(dataset_version.assignments.list(page_size=10))
            5
        """
        req = management_pb2.ListDatasetVersionAssignmentsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListDatasetVersionAssignments(req)
        return [
            DatasetVersionAssignment.from_proto(
                x, client=self.client, current_run=self.run_name
            )
            for x in resp.assignments
        ]

    def list_all(self) -> Pager[DatasetVersionAssignment]:
        """List all dataset version assignments.

        Pages through all dataset versions using an iterator.

        Returns:
            A iterator of all DatasetVersionAssignment.

        Examples:
            >>> ... # Assume run is defined
            >>> dataset_version = run.datasets.create("test_dataset").dataset_versions.create()
            >>> model_versions = [
                    run.models.create(f"test_model_{i}").model_versions.create()
                    for i in range(5)
                ]
            >>> dv_assignments = [
                    dataset_version.assignments.create(resource_name=mv.name)
                    for mv in model_versions
                ]
            >>> len(list(dataset_version.assignments.list_all()))
            5
        """

        def next_page(next_page_token):
            req = management_pb2.ListDatasetVersionAssignmentsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListDatasetVersionAssignments(req)
            return (
                [
                    DatasetVersionAssignment.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.assignments
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def delete(self, id: str) -> None:
        """Delete a dataset version assignment.

        Arguments:
            id: DatasetVersionAssignment name or id.

        Examples:
            >>> ... # Assume dataset_version and model_version are defined
            >>> dv_assignment = dataset_version.assignments.create(resource_name=model_version.name)
            >>> len(dataset_version.assignments.list_all())
            1
            >>> dataset_version.assignments.delete(id=dv_assignment.id)
            >>> len(list(dataset_version.assignments.list_all()))
            0
        """

        req = management_pb2.DeleteDatasetVersionAssignmentRequest(name=self.name(id))
        self.client._management.DeleteDatasetVersionAssignment(req)

    def update(
        self,
        dataset_version_assignment: DatasetVersionAssignment,
        paths: List[str],
    ) -> DatasetVersionAssignment:
        """Update DatasetVersionAssignment.

        Arguments:
            paths: A list of paths to be updated.
            dataset_version_assignment: DatasetVersionAssignment object containing updated fields.

        Returns:
            An updated DatasetVersionAssignment.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
        """

        req = management_pb2.UpdateDatasetVersionAssignmentRequest(
            assignment=dataset_version_assignment.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateDatasetVersionAssignment(req)
        return DatasetVersionAssignment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class DatasetVersionAssignment(Resource, types.DatasetVersionAssignment):
    """Dataset version resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/datasets/{dataset}/versions/{version}/assignments/{assignment}"

    _manager: DatasetVersionAssignmentManager
    """DatasetVersionAssignment manager."""

    def _init(self):
        self._manager = DatasetVersionAssignmentManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )

    def update(self, paths: List[str]) -> DatasetVersionAssignment:
        """Update DatasetVersionAssignment.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated DatasetVersionAssignment.

        Examples:
            >>> ...
        """
        return self._manager.update(paths=paths, dataset_version_assignment=self)

    def add_tags(self, tags: dict[str, str]) -> DatasetVersionAssignment:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated DatasetVersionAssignment.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> dsv = dataset_version.assignments.get("test-assignment")
            >>> dsv.add_tags({"color": "blue", "fruit": "apple"})
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(dataset_version_assignment=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> DatasetVersionAssignment:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated DatasetVersionAssignment.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> dsv = dataset_version.assignments.get("test-assignment")
            >>> dsv.remove_tags({"color", "fruit"})
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(dataset_version_assignment=self, paths=["tags"])
