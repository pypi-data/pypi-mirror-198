from __future__ import annotations
from typing import Iterator, List, Optional
from continual.python.sdk.metrics import MetricsManager

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.checks import ChecksManager
from continual.python.sdk.metadata import MetadataManager


class BatchPredictionManager(Manager):
    """Manages Batch Prediction resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/batchPredictions/{batch_prediction_job}"

    def create(
        self,
        id: Optional[str] = None,
        model_version: Optional[str] = None,
        prediction_count: Optional[int] = None,
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> BatchPrediction:
        """Get batch prediction job.

        Arguments:
            id: Batch Prediction  name or id.
            model_version: Name of the model version to use for prediction
            prediction_count: Number of predictions in the batch prediction
            tags: Tags to be added to the batch prediction
            replace_if_exists: If true, update the existing batch prediction if it exists, else throw an error.
        Returns
            A Batch prediction.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> model.batch_predictions.create(model_version=model_version.name, prediction_count=150, tags={"type":"daily", "cat": "test"})
            <BatchPrediction object {'name': 'projects/continual-test-proj/environments/production/models/example-model/batchPredictions/cgcfu7a5lsrvj7pl70r0',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcfsfa5lsrvj7pl70p0',
            'create_time': '2023-03-21T00:49:33.759597Z', 'prediction_count': '150', 'run': 'projects/continual-test-proj/environments/production/runs/example-run',
            'tags': {'cat': 'test', 'type': 'daily'}, 'created_by': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0', 'error_message': '', 'stack_trace': ''}>
            >>> model.batch_predictions.create(model_version=model_version.name, prediction_count=2000, tags={"type":"daily", "cat": "train"}, replace_if_exists=True)
            <BatchPrediction object {'name': 'projects/continual-test-proj/environments/production/models/example-model/batchPredictions/cgcfv5q5lsrvj7pl70s0',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcfsfa5lsrvj7pl70p0',
            'create_time': '2023-03-21T00:51:35.826307Z', 'prediction_count': '2000', 'run': 'projects/continual-test-proj/environments/production/runs/example-run',
            'tags': {'type': 'daily', 'cat': 'train'}, 'created_by': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0', 'error_message': '', 'stack_trace': ''}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateBatchPredictionRequest(
            parent=self.parent,
            batch_prediction=BatchPrediction(
                run=self.run_name,
                model_version=self.name(
                    model_version,
                    self.parent,
                    f"{self.parent}/versions/{id}",
                ),
                prediction_count=prediction_count,
                tags=tags,
                current_run=self.run_name,
            ).to_proto(),
            batchprediction_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateBatchPrediction(req)
        return BatchPrediction.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def get(self, id: str) -> BatchPrediction:
        """Get batch prediction job.

        Arguments:
            id: Batch Prediction name or id.

        Returns
            A Batch prediction.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> batchprediction = model.batch_predictions.create(model_version=model_version.name)
            >>> model.batch_predictions.get(batchprediction.id)     # Get from id
            <BatchPrediction object {'name': 'projects/continual-test-proj/environments/production/models/example-model/batchPredictions/cgcg0ni5lsrvj7pl70t0',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcfsfa5lsrvj7pl70p0',
            'create_time': '2023-03-21T00:54:54.047254Z', 'run': 'projects/continual-test-proj/environments/production/runs/example-run',
            created_by': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0', 'prediction_count': '0', 'error_message': '', 'stack_trace': '', 'tags': {}}>
            >>> model.batch_predictions.get(batchprediction.name)   # Get from name
            <BatchPrediction object {'name': 'projects/continual-test-proj/environments/production/models/example-model/batchPredictions/cgcg0ni5lsrvj7pl70t0',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcfsfa5lsrvj7pl70p0',
            'create_time': '2023-03-21T00:54:54.047254Z', 'run': 'projects/continual-test-proj/environments/production/runs/example-run',
            created_by': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0', 'prediction_count': '0', 'error_message': '', 'stack_trace': '', 'tags': {}}>
        """
        req = management_pb2.BatchPredictionRequest(name=self.name(id))
        resp = self.client._management.GetBatchPrediction(req)
        return BatchPrediction.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        default_sort_order: str = "ASC",
        order_by: Optional[str] = None,
    ) -> List[BatchPrediction]:
        """List batch prediction jobs.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of batch prediction jobs.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> batch_predictions = [model.batch_predictions.create(id=f"test-{10-i}", model_version=model_version.name, prediction_count=10*i) for i in range(10)]
            >>> [bp.prediction_count for bp in model.batch_predictions.list(page_size=20))] # Sort by create time ascending by default
            [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
            >>> [bp.prediction_count for bp in model.batch_predictions.list(page_size=20, order_by="prediction_count", default_sort_order="DESC"))] # Sort by prediction count descending
            [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
            >>> [bp.id for bp in model.batch_predictions.list(page_size=20, order_by="id desc"))] # Sort by prediction count ascending
            ['test-9', 'test-8', 'test-7', 'test-6', 'test-5', 'test-4', 'test-3', 'test-2' 'test-10', 'test-1']
        """
        req = management_pb2.ListBatchPredictionsRequest(
            parent=self.parent,
            default_sort_order=default_sort_order,
            order_by=order_by,
            page_size=page_size,
        )
        resp = self.client._management.ListBatchPredictions(req)
        return [
            BatchPrediction.from_proto(u, client=self.client, current_run=self.run_name)
            for u in resp.batch_predictions
        ]

    def list_all(self) -> Iterator[BatchPrediction]:
        """List all batch prediction jobs.

        Pages through all batch prediction jobs using an iterator.

        Returns:
            A iterator of all batch prediction jobs.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> batchpredictions = [model.batch_predictions.create(id=f"test-{i}", model_version=model_version.name, prediction_count=i) for i in range(10)]
            >>> [bp.id for bp in model.batch_predictions.list_all()]     # List all batch predictions
            ['test-0', 'test-1', 'test-2', 'test-3', 'test-4', 'test-5', 'test-6', 'test-7', 'test-8', 'test-9']
        """

        def next_page(next_page_token):
            req = management_pb2.ListBatchPredictionsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListBatchPredictions(req)
            return (
                [
                    BatchPrediction.from_proto(
                        u, client=self.client, current_run=self.run_name
                    )
                    for u in resp.batch_predictions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        batch_prediction: BatchPrediction,
    ) -> BatchPrediction:
        """Update batch prediction.

        Arguments:
            paths: A list of paths to be updated.
            batch_prediction: BatchPrediction object containing updated fields.

        Returns:
            An updated batch prediction.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> batch_prediction = model.batch_predictions.create(id="test", model_version=model_version.name, prediction_count=10)
            >>> batch_prediction.prediction_count
            10
            >>> batch_prediction.prediction_count = 20
            >>> updated_bp = model.batch_predictions.update(paths=["prediction_count"], batch_prediction=batch_prediction)
            >>> updated_bp.prediction_count
            20
        """

        req = management_pb2.UpdateBatchPredictionRequest(
            batch_prediction=batch_prediction.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateBatchPrediction(req)
        return BatchPrediction.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def _get_latest_batch_prediction(self) -> BatchPrediction:
        """Get latest batchprediction.

        Returns:
            The most recently created BatchPrediction.

        Examples:
            >>> ...
        """
        req = management_pb2.GetLatestBatchPredictionRequest(parent=self.parent)
        resp = self.client._management.GetLatestBatchPrediction(req)
        return BatchPrediction.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class BatchPrediction(Resource, types.BatchPrediction):
    """BatchPrediction resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/batchPredictions/{batch_prediction_job}"

    _manager: BatchPredictionManager
    """BatchPrediction manager"""

    _metrics: MetricsManager
    """Metrics Manager"""

    _artifacts: ArtifactsManager
    """Artifacts Manager"""

    _metadata: MetadataManager
    """Metadata Manager"""

    _checks: ChecksManager

    def _init(self):
        self._manager = BatchPredictionManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._metrics = MetricsManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._checks = ChecksManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def artifacts(self) -> ArtifactsManager:
        """Artifacts Manager."""
        return self._artifacts

    @property
    def metadata(self) -> MetadataManager:
        """Metadata Manager."""
        return self._metadata

    @property
    def metrics(self) -> MetricsManager:
        """Metrics Manager."""
        return self._metrics

    @property
    def checks(self) -> ChecksManager:
        """Checks manager."""
        return self._checks

    def update(self, paths: List[str]) -> BatchPrediction:
        """Update BatchPrediction.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated BatchPrediction.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> batch_prediction = model.batch_predictions.create(id="test", model_version=model_version.name, prediction_count=10)
            >>> batch_prediction.prediction_count
            10
            >>> batch_prediction.prediction_count = 20
            >>> updated_bp = batch_prediction.update(paths=["prediction_count"])
            >>> updated_bp.prediction_count
            20
        """
        return self._manager.update(paths=paths, batch_prediction=self)

    def add_tags(self, tags: dict[str, str]) -> BatchPrediction:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated BatchPrediction.

        Examples:
            >>> # batch_prediction is a BatchPrediction object with tags {"color": "red"}
            >>> batch_prediction.tags
            {'color': 'red'}
            >>> updated_bp = batch_prediction.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_bp.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(batch_prediction=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> BatchPrediction:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated BatchPrediction.

        Examples:
            >>> # batch_prediction is a BatchPrediction object with tags {"color": "red"}
            >>> batch_prediction.tags
            {'color': 'red'}
            >>> updated_bp = batch_prediction.remove_tags(["color", "fruit"])
            >>> updated_bp.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(batch_prediction=self, paths=["tags"])
