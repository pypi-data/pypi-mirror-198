from __future__ import annotations
from typing import List, Optional
from continual.python.sdk.metrics import MetricsManager
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.metadata import MetadataManager
from continual.python.sdk.checks import ChecksManager


class ExperimentManager(Manager):
    """Manages experiment resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/versions/{version}/experiments/{experiment}"

    def create(
        self,
        id: Optional[str] = "",
        error_message: Optional[str] = "",
        stack_trace: Optional[str] = "",
        performance_metric_name: Optional[str] = "",
        performance_metric_val: Optional[float] = 0.0,
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> Experiment:
        """Create experiment.

        Arguments:
            id: Experiment name or id.
            error_message: Error message.
            stack_trace: Stack trace.
            performance_metric_name: Primary metric name.
            performance_metric_val: Primary metric value.
            tags: Tags to be associated with the experiment.
            replace_if_exists: If true, update the experiment if it already exists.

        Returns
            An experiment.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> model_version.experiments.create()
            <Experiment object {'name': 'projects/test_project_1/environments/test_env/models/test_model/versions/cegl9qq5lsrkc0osu0ug/experiments/ceglm7a5lsrkc0osu120',
            'run_name': 'projects/test_project_1/environments/test_env/runs/test_run', 'create_time': '2022-12-20T06:50:05.351093Z',
            'performance_metric_name': '', 'performance_metric_val': 0.0, 'training_config': '', 'error_message': '', 'stack_trace': ''}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateExperimentRequest(
            parent=self.parent,
            experiment=Experiment(
                error_message=error_message,
                stack_trace=stack_trace,
                performance_metric_name=performance_metric_name,
                performance_metric_val=performance_metric_val,
                tags=tags,
                run=self.run_name,
                current_run=self.run_name,
            ).to_proto(),
            experiment_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateExperiment(req)
        return Experiment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def get(self, id: str) -> Experiment:
        """Get experiment.

        Arguments:
            id: Experiment name or id.

        Returns
            An experiment.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> experiment = model_version.experiments.create()
            >>> model_version.experiments.get(experiment.id)
            <Experiment object {'name': 'projects/test_project_1/environments/test_env/models/test_model/versions/cegl9qq5lsrkc0osu0ug/experiments/ceglm7a5lsrkc0osu120',
            'run_name': 'projects/test_project_1/environments/test_env/runs/test_run', 'create_time': '2022-12-20T06:50:05.351093Z',
            'performance_metric_name': '', 'performance_metric_val': 0.0, 'training_config': '', 'error_message': '', 'stack_trace': ''}>
        """
        req = management_pb2.GetExperimentRequest(name=self.name(id))
        resp = self.client._management.GetExperiment(req)
        return Experiment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
        all_projects: bool = False,
    ) -> List[Experiment]:
        """List experiments.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.
            all_projects:  Whether to include all instances of this resource from the project or just from the current parent.

        Returns:
            A list of experiments.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> experiments = [model_version.experiments.create() for _ in range(100)]
            >>> len(model_version.experiments.list(page_size=10))
            10
            >>> len(model_version.experiments.list(page_size=50))
            50
        """
        req = management_pb2.ListExperimentsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
            all_projects=all_projects,
        )
        resp = self.client._management.ListExperiments(req)
        return [
            Experiment.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.experiments
        ]

    def list_all(self) -> Pager[Experiment]:
        """List all experiments.

        Pages through all experiments using an iterator.

        Returns:
            A iterator of all experiments.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> experiments = [model_version.experiments.create() for _ in range(100)]
            >>> len(list(model_version.experiments.list_all()))
            100
        """

        def next_page(next_page_token):
            req = management_pb2.ListExperimentsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListExperiments(req)
            return (
                [
                    Experiment.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.experiments
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        experiment: Experiment,
    ) -> Experiment:
        """Update Experiment.

        Arguments:
            paths: A list of paths to be updated.
            experiment: Experiment object containing updated fields.

        Returns:
            An updated Experiment.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
        """

        req = management_pb2.UpdateExperimentRequest(
            experiment=experiment.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateExperiment(req)
        return Experiment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class Experiment(Resource, types.Experiment):
    """Experiment resource."""

    _manager: ExperimentManager
    """Experiment manager."""

    _checks: ChecksManager

    _metrics: MetricsManager
    """Metrics Manager"""

    _artifacts: ArtifactsManager
    """Artifacts Manager"""

    _metadata: MetadataManager
    """Metadata Manager"""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/versions/{version}/experiments/{experiment}"

    def _init(self):
        self._manager = ExperimentManager(
            parent=self.parent, client=self.client, run_name=self.current_run
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
    def metrics(self) -> MetricsManager:
        """Metrics Manager"""
        return self._metrics

    @property
    def artifacts(self) -> ArtifactsManager:
        """Artifacts Manager"""
        return self._artifacts

    @property
    def metadata(self) -> MetadataManager:
        """Metadata Manager"""
        return self._metadata

    @property
    def checks(self) -> ChecksManager:
        """Checks manager."""
        return self._checks

    def update(self, paths: List[str]) -> Experiment:
        """Update Experiment.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Experiment.

        Examples:
            >>> ...
        """
        return self._manager.update(paths=paths, experiment=self)

    def add_tags(self, tags: dict[str, str]) -> Experiment:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Experiment.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> experiment =  model_version.experiments.get("test-experiment")
            >>> experiment.add_tags({"color": "blue", "fruit": "apple"})
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(experiment=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Experiment:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Experiment.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> experiment =  model_version.experiments.get("test-experiment")
            >>> experiment.remove_tags(["color", "fruit"])
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(experiment=self, paths=["tags"])
