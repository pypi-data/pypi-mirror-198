from __future__ import annotations

from typing import List, Optional
from continual.python.sdk.batchpredictions import (
    BatchPredictionManager,
)
from continual.python.sdk.events import EventManager
from continual.python.sdk.checks import ChecksManager
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager

# hide experiments until futher review
# from continual.python.sdk.experiments import ExperimentManager
from continual.python.sdk.promotions import PromotionManager
from continual.python.sdk.metrics import MetricsManager
from continual.python.sdk.artifacts import ArtifactsManager

from continual.python.sdk.metadata import MetadataManager


class ModelVersionManager(Manager):
    """Manages Model Version resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/versions/{version}"

    def create(
        self,
        id: Optional[str] = "",
        error_message: Optional[str] = "",
        stack_trace: Optional[str] = "",
        performance_metric_name: Optional[str] = "",
        performance_metric_val: Optional[float] = 0.0,
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: Optional[bool] = False,
    ) -> ModelVersion:
        """Create a model version for local development

        Arguments:
            id: Optional model version id.
            error_message: Error message associated with this model version
            stack_trace: Stack trace associated with an error.
            performance_metric_name: Name of the primary metric.
            performance_metric_val: Value of the primary metric.
            tags: Optional tags to associate with this model version.
            replace_if_exists: If true, update the model version if it already exists.

        Returns
            A Model Version.

        Examples:
            >>> # model is a Model object
            >>> model.model_versions.create()
            <ModelVersion object {'name': 'projects/test_proj_4/environments/test_env/models/my_model/versions/ceg98ea5lsrt9r5a8l10',
            'run_name': 'projects/test_proj_4/environments/test_env/runs/ceg93ji5lsrt9r5a8kt0',
            'create_time': '2022-12-19T16:41:29.232614Z', 'update_time': '2022-12-19T16:41:29.232614Z',
            'experiment_name': '', 'error_message': '', 'stack_trace': '', 'training_row_count': '0', 'validation_row_count': '0',
            'test_row_count': '0', 'performance_metric': '', 'performance_metric_val': 0.0, 'promotion': '', 'promoted': False}>
            >>> model.model_versions.create(id="my-version")
            <ModelVersion object {'name': 'projects/test_proj_4/environments/test_env/models/my_model/versions/my-version',
            'run_name': 'projects/test_proj_4/environments/test_env/runs/ceg93ji5lsrt9r5a8kt0',
            'create_time': '2022-12-19T16:41:29.232614Z', 'update_time': '2022-12-19T16:41:29.232614Z',
            'experiment_name': '', 'error_message': '', 'stack_trace': '', 'training_row_count': '0', 'validation_row_count': '0',
            'test_row_count': '0', 'performance_metric': '', 'performance_metric_val': 0.0, 'promotion': '', 'promoted': False}>
            >>> model.model_versions.create(id="my-version", error_message="Model failed to train", stack_trace=traceback.format_exc())
            <ModelVersion object {'name': 'projects/continual-test-proj/environments/production/models/example-model/versions/my-version',
            'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og', 'error_message': 'Model failed to train',
            'create_time': '2023-03-22T01:37:42.108358Z', 'update_time': '2023-03-22T01:37:42.108358Z',
            'signature': {'inputs': [], 'outputs': []}, 'stack_trace': '', 'performance_metric_name': '', 'performance_metric_val': 0.0,
            'feature_importances': [], 'tags': {}}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateModelVersionRequest(
            parent=self.parent,
            model_version=ModelVersion(
                run=self.run_name,
                error_message=error_message,
                stack_trace=stack_trace,
                performance_metric_name=performance_metric_name,
                performance_metric_val=performance_metric_val,
                tags=tags,
                current_run=self.run_name,
            ).to_proto(),
            model_version_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateModelVersion(req)
        return ModelVersion.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def get(self, id: str) -> ModelVersion:
        """Get model version.

        Arguments:
            id: Model name or id.

        Returns
            An Model Version.

        Examples:
            >>> # model is a Model object
            >>> model_version = model.model_versions.create()
            >>> model.model_versions.get(model_version.id)
            <ModelVersion object {'name': 'projects/test_proj_4/environments/test_env/models/my_model/versions/ceg98ea5lsrt9r5a8l10',
            'run_name': 'projects/test_proj_4/environments/test_env/runs/ceg93ji5lsrt9r5a8kt0',
            'create_time': '2022-12-19T16:41:29.232614Z', 'update_time': '2022-12-19T16:41:29.232614Z',
            'experiment_name': '', 'error_message': '', 'stack_trace': '', 'training_row_count': '0', 'validation_row_count': '0',
            'test_row_count': '0', 'performance_metric': '', 'performance_metric_val': 0.0, 'promotion': '', 'promoted': False}>
        """
        req = management_pb2.GetModelVersionRequest(name=self.name(id))
        resp = self.client._management.GetModelVersion(req)
        return ModelVersion.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[ModelVersion]:
        """List model versions.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of ModelVersions.

        Examples:
            >>> # model is a Model object
            >>> model_versions = [model.model_versions.create() for _ in range(3)]
            >>> first_model_version = model.model_versions.list(page_size=10)[0]  # Get first model version
            >>> latest_model_version = model.model_versions.list(page_size=10, default_sort_order="DESC")[0] # Get latest model version
        """
        req = management_pb2.ListModelVersionsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListModelVersions(req)
        return [
            ModelVersion.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.model_versions
        ]

    def list_all(self) -> Pager[ModelVersion]:
        """List all model versions.

        Pages through all model versions using an iterator.

        Returns:
            A iterator of all model versions.

        Examples:
            >>> # model is a Model object
            >>> mvs = [model.model_versions.create() for _ in range(3)]
            >>> len(list(model.model_versions.list_all())) # List all model versions
            3
        """

        def next_page(next_page_token):
            req = management_pb2.ListModelVersionsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListModelVersions(req)
            return (
                [
                    ModelVersion.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.model_versions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        model_version: ModelVersion,
    ) -> ModelVersion:
        """Update model version.

        Arguments:
            paths: A list of paths to be updated.
            model_version: Model version object containing updated fields.

        Returns:
            An updated model version.

        Examples:
            >>> # model is a Model object
            >>> model_version = model.model_versions.create()
            >>> model_version.tags
            {}
            >>> model_version.tags = {"tag1": "value1", "tag2": "value2"}
            >>> updated_mv = model.model_versions.update(model_version=model_version, paths=["tags"])
            >>> updated_mv.tags
            {'tag1': 'value1', 'tag2': 'value2'}

        """

        req = management_pb2.UpdateModelVersionRequest(
            model_version=model_version.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateModelVersion(req)
        return ModelVersion.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def _get_latest_model_version(self) -> ModelVersion:
        """Get latest model version.

        Returns:
            The most recently created ModelVersion.

        Examples:
            >>> ...
        """
        req = management_pb2.GetLatestModelVersionRequest(parent=self.parent)
        resp = self.client._management.GetLatestModelVersion(req)
        return ModelVersion.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class ModelVersion(Resource, types.ModelVersion):
    """Model version resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/versions/{version}"

    _manager: ModelVersionManager

    # hide experiments until futher review
    # _experiments: ExperimentManager

    _events: EventManager

    _promotions: PromotionManager

    _checks: ChecksManager

    _batch_predictions: BatchPredictionManager

    _metrics: MetricsManager

    _artifacts: ArtifactsManager

    _metadata: MetadataManager

    def _init(self):
        self._manager = ModelVersionManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._promotions = PromotionManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._batch_predictions = BatchPredictionManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        # hide experiments until futher review
        # self._experiments = ExperimentManager(
        #     parent=self.name, client=self.client, run_name=self.current_run
        # )
        self._events = EventManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._metrics = MetricsManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

        self._checks = ChecksManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def promotions(self) -> PromotionManager:
        """Promotion manager."""
        return self._promotions

    @property
    def batch_predictions(self) -> BatchPredictionManager:
        """Batch Prediction manager."""
        return self._batch_predictions

    # hide experiments until futher review
    # @property
    # def experiments(self) -> ExperimentManager:
    #     """Experiment manager."""
    #     return self._experiments

    @property
    def metrics(self) -> MetricsManager:
        """Metrics manager."""
        return self._metrics

    @property
    def artifacts(self) -> ArtifactsManager:
        """Artifacts manager."""
        return self._artifacts

    @property
    def checks(self) -> ChecksManager:
        """Checks manager."""
        return self._checks

    @property
    def metadata(self) -> MetadataManager:
        """Metadata manager."""
        return self._metadata

    @property
    def events(self) -> EventManager:
        """Event manager."""
        return self._events

    def update(
        self,
        paths: List[str],
    ) -> ModelVersion:
        """Update model version.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated model version.

        Examples:
            >>> # model is a Model object
            >>> model_version = model.model_versions.create()
            >>> model_version.error_message
            ''
            >>> model_version.error_message = 'error'
            >>> updated_mv = model_version.update(paths=["error_message"])
            >>> updated_mv.error_message
            'error'
        """

        if "signature" in paths:
            pb_signature = types.ModelVersionSignature(inputs=[], outputs=[])
            if "inputs" in self.signature:
                for input in self.signature["inputs"]:
                    if "name" in input and "type" in input:
                        pb_signature.inputs.append(
                            types.ModelVersionSignatureInput(
                                name=input["name"], type=input["type"]
                            )
                        )
            if "outputs" in self.signature:
                for output in self.signature["outputs"]:
                    if "type" in output:
                        pb_signature.outputs.append(
                            types.ModelVersionSignatureOutput(type=output["type"])
                        )

            self.signature = pb_signature
        return self._manager.update(paths=paths, model_version=self)

    def add_tags(self, tags: dict[str, str]) -> ModelVersion:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated ModelVersion.

        Examples:
            >>> # model_version is a ModelVersion object with tags {"color": "red"}
            >>> model_version.tags
            {'color': 'red'}
            >>> updated_mv = model_versi on.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_mv.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(model_version=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> ModelVersion:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated ModelVersion.

        Examples:
            >>> # model_version is a ModelVersion object with tags {"color": "red"}
            >>> model_version.tags
            {'color': 'red'}
            >>> updated_dv = model_version.remove_tags(["color", "fruit"])
            >>> updated_dv.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(model_version=self, paths=["tags"])
