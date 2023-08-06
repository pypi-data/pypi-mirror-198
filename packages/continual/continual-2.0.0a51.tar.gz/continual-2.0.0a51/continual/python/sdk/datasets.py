from __future__ import annotations
from typing import List, Optional
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.checks import ChecksManager
from continual.python.sdk.metrics import MetricsManager
from continual.python.sdk.dataset_versions import DatasetVersion, DatasetVersionManager

from continual.python.sdk.metadata import MetadataManager


from continual.python.sdk.batchpredictions import (
    BatchPredictionManager,
)


class DatasetManager(Manager):
    """Manages dataset resources."""

    name_pattern: str = (
        "projects/{project}/environments/{environment}/datasets/{dataset}"
    )

    def create(
        self,
        id: Optional[str] = "",
        display_name: Optional[str] = "",
        description: Optional[str] = "",
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> Dataset:
        """Create dataset.

        Arguments:
            id: Dataset name or id.
            display_name: Dataset name or id.
            description: A brief description of this dataset.
            tags: A dict of tags to add to this dataset.
            replace_if_exists: If True, this call will update the dataset with this ID if it exists else create it.If false, it will throw an error.

        Returns
            A Dataset.

        Examples:
            >>> # run is a Run object
            >>> run.datasets.create(
            ...        id="example-dataset",
            ...        display_name="My customer churn dataset",
            ...        description="A dataset of customer churn data.",
            ...        tags={"source": "csv", "period": "daily"}
            ... )
            <Dataset object {'name': 'projects/continual-test-proj/environments/production/datasets/example-dataset',
            'description': 'A dataset of customer churn data.', 'author': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0',
            'display_name': 'My customer churn dataset', 'create_time': '2023-03-21T16:32:49.859648Z', 'update_time': '2023-03-21T16:32:49.859648Z',
            'run': 'projects/continual-test-proj/environments/production/runs/cgcto925lsrvj7pl723g', 'tags': {'source': 'csv', 'period': 'daily'}}>
            >>> # Attempt to create a dataset with the same ID.
            >>> run.datasets.create(
            ...        id="example-dataset",
            ...        display_name="My customer churn dataset",
            ...        description="A dataset of customer churn data.",
            ...        tags={"source": "sql", "period": "daily"}
            ... )
            Exception: ('Resource already exists.', {'name': 'projects/continual-test-proj/environments/production/datasets/example-dataset'})
            >>> # Create a dataset with the same ID, but replace it.
            >>> run.datasets.create(
            ...        id="example-dataset",
            ...        display_name="My customer churn dataset",
            ...        description="A dataset of customer churn data.",
            ...        tags={"source": "sql", "period": "daily"},
            ...        replace_if_exists=True
            ... )
            <Dataset object {'name': 'projects/continual-test-proj/environments/production/datasets/example-dataset',
            'description': 'A dataset of customer churn data.', 'author': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0',
            'display_name': 'My customer churn dataset', 'create_time': '2023-03-21T16:32:49.859648Z', 'update_time': '2023-03-21T16:36:58.058267Z',
            'run': 'projects/continual-test-proj/environments/production/runs/cgcto925lsrvj7pl723g', 'tags': {'source': 'txt', 'period': 'daily'}}>
        """

        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateDatasetRequest(
            parent=self.parent,
            dataset=Dataset(
                description=description,
                display_name=display_name,
                run=self.run_name,
                tags=tags,
                current_run=self.run_name,
            ).to_proto(),
            dataset_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateDataset(req)
        return Dataset.from_proto(resp, client=self.client, current_run=self.run_name)

    def get(self, id: str) -> Dataset:
        """Get dataset.

        Arguments:
            id: Dataset name or id.

        Returns
            A Dataset.

        Examples:
            >>> # run is a Run object
            >>> run.datasets.create(
            ...        id="example-dataset",
            ...        display_name="My customer churn dataset",
            ...        description="A dataset of customer churn data.",
            ...        tags={"source": "csv", "period": "daily"}
            ... )
            >>> run.datasets.get("example-dataset")
            <Dataset object {'name': 'projects/continual-test-proj/environments/production/datasets/example-dataset',
            'description': 'A dataset of customer churn data.', 'author': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0',
            'display_name': 'My customer churn dataset', 'create_time': '2023-03-21T16:32:49.859648Z', 'update_time': '2023-03-21T16:32:49.859648Z',
            'run': 'projects/continual-test-proj/environments/production/runs/cgcto925lsrvj7pl723g', 'tags': {'source': 'csv', 'period': 'daily'}}>
        """
        req = management_pb2.GetDatasetRequest(name=self.name(id))
        resp = self.client._management.GetDataset(req)
        return Dataset.from_proto(resp, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[Dataset]:
        """List dataset.

        Note: Datasets may be listed across all runs, not just the run in which
        they were created.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Datasets.

        Examples:
            >>> # run is a Run object
            >>> ds = [run.datasets.create(id=f"ds-{i}", display_name=f"Dataset ranked {10-i}", description=f"Customer churn dataset {i%2}") for i in range(10)]
            >>> [d.id for d in run.datasets.list(page_size=10, default_sort_order="DESC")]
            ['ds-9', 'ds-8', 'ds-7', 'ds-6', 'ds-5', 'ds-4', 'ds-3', 'ds-2', 'ds-1', 'ds-0']
            >>> [d.id for d in run.datasets.list(page_size=10, order_by="display_name")]
            ['ds-9', 'ds-0', 'ds-8', 'ds-7', 'ds-6', 'ds-5', 'ds-4', 'ds-3', 'ds-2', 'ds-1']
            >>> [d.id for d in run.datasets.list(page_size=20, order_by="description asc, id", default_sort_order="desc")]
            ['ds-8', 'ds-6', 'ds-4', 'ds-2', 'ds-0', 'ds-9', 'ds-7', 'ds-5', 'ds-3', 'ds-1']
        """
        req = management_pb2.ListDatasetsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListDatasets(req)
        return [
            Dataset.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.datasets
        ]

    def list_all(self) -> Pager[Dataset]:
        """List all Datasets.

        Pages through all datasets using an iterator in
        the default sort order (ascending by create_time and name).

        Returns:
            A iterator of all dataset.

        Examples:
            >>> # run is a Run object
            >>> ds = [run.datasets.create(id=f"ds-{i}", display_name=f"Dataset ranked {10-i}", description=f"Customer churn dataset {i%2}") for i in range(10)]
            >>> [d.id for d in run.datasets.list_all()]
            ['ds-0', 'ds-1', 'ds-2', 'ds-3', 'ds-4', 'ds-5', 'ds-6', 'ds-7', 'ds-8', 'ds-9']
        """

        def next_page(next_page_token):
            req = management_pb2.ListDatasetsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListDatasets(req)
            return (
                [
                    Dataset.from_proto(x, client=self.client, current_run=self.run_name)
                    for x in resp.datasets
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        dataset: Dataset,
        paths: List[str],
    ) -> Dataset:
        """Update Dataset.

        Arguments:
            dataset: Dataset object containing updated fields.
            paths: A list of paths to be updated.

        Returns:
            An updated Dataset.

        Examples:
            >>> # run is a Run object
            >>> ds = run.datasets.create(id="ds-1", display_name="Dataset ranked 1", description="Customer churn dataset")
            >>> ds.display_name
            "Dataset ranked 1"
            >>> ds.display_name = "Dataset ranked 2"
            >>> updated_ds = run.datasets.update(dataset=ds, paths=["display_name"])
            >>> updated_ds.display_name
            "Dataset ranked 2"
        """

        req = management_pb2.UpdateDatasetRequest(
            dataset=dataset.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateDataset(req)
        return Dataset.from_proto(resp, client=self.client, current_run=self.run_name)


class Dataset(Resource, types.Dataset):
    """Dataset resource."""

    name_pattern: str = (
        "projects/{project}/environments/{environment}/datasets/{dataset}"
    )
    _manager: DatasetManager
    """Dataset Manager."""

    _dataset_versions: DatasetVersionManager
    """Dataset version manager."""

    _batch_predictions: BatchPredictionManager
    """Batch Prediction manager."""

    _metadata: MetadataManager
    """Metadata Manager"""

    _checks: ChecksManager
    """Checks Manager"""

    _metrics: MetricsManager
    """Metrics Manager"""

    def _init(self):
        self._manager = DatasetManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._dataset_versions = DatasetVersionManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._batch_predictions = BatchPredictionManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._checks = ChecksManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._metrics = MetricsManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def dataset_versions(self) -> DatasetVersionManager:
        """Dataset version manager."""
        return self._dataset_versions

    @property
    def batch_predictions(self) -> BatchPredictionManager:
        """Batch Prediction manager."""
        return self._batch_predictions

    @property
    def metadata(self) -> MetadataManager:
        """Metadata Manager"""
        return self._metadata

    @property
    def checks(self) -> ChecksManager:
        """Checks manager."""
        return self._checks

    @property
    def metrics(self) -> MetricsManager:
        """Metrics Manager"""
        return self._metrics

    def update(self, paths: List[str]) -> Dataset:
        """Update Dataset.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Dataset.

        Examples:
            >>> # ds is a Dataset object
            >>> ds.display_name
            "Dataset ranked 1"
            >>> ds.display_name = "Dataset ranked 2"
            >>> updated_ds = ds.update(paths=["display_name"])
            >>> updated_ds.display_name
            "Dataset ranked 2"
        """
        return self._manager.update(paths=paths, dataset=self)

    def latest_dataset_version(self) -> DatasetVersion:
        """List the dataset versions on this dataset and return the most recently
        created one.

        Returns:
            The most recently created DatasetVersion.

        Examples:
            >>> # ds is a Dataset object
            >>> versions = [ds.dataset_versions.create(id=f"ds-{i}") for i in range(10)]
            >>> ds.latest_dataset_version().id
            'ds-9'
        """
        return self._dataset_versions._get_latest_dataset_version()

    def add_tags(self, tags: dict[str, str]) -> Dataset:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Dataset.

        Examples:
            >>> # dataset is a Dataset object with tags {"color": "red"}
            >>> dataset.tags
            {'color': 'red'}
            >>> updated_dataset = dataset.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_dataset.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(dataset=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Dataset:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Dataset.

        Examples:
            >>> # dataset is a Dataset object with tags {"color": "red"}
            >>> dataset.tags
            {'color': 'red'}
            >>> updated_dataset = dataset.remove_tags(["color", "fruit"])
            >>> updated_dataset.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(dataset=self, paths=["tags"])
