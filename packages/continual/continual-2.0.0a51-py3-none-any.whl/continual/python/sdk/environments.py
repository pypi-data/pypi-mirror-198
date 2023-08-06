from __future__ import annotations
from typing import List, Optional
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.datasets import DatasetManager
from continual.python.sdk.runs import RunManager
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.models import ModelManager


class EnvironmentManager(Manager):
    """Manages environment resources."""

    name_pattern: str = "projects/{project}/environments/{environment}"

    def create(
        self,
        id: Optional[str] = "",
        source: Optional[str] = "",
        env_type: Optional[str] = "",
        is_protected: bool = False,
        is_ephemeral: bool = False,
        replace_if_exists: bool = False,
    ) -> Environment:
        """Create an environment.

        New environments are identified by a unique ID within
        their parent project.

        Arguments:
            id: Environment ID.
            source: An environment or project that this environment was created from.
            env_type: The "role" of this environment in the workflow: unspecified, main, trunk, dev, code_review, etc..
            is_protected: If True, environment is protected. A protected environment can only be pushed to by CI/CD when connected.
            is_ephemeral: If True, environment is ephemeral. Ephemeral environments are automated, isolated, protected, and short-lived.
            replace_if_exists: If True and the environment already exists, return the existing
                environment.  If False and the environment already exists, raise an error.

        Returns:
            A new environment.

        Examples:
            >>> # project is a Project object
            >>> project.environments.create(id="staging")
            <Environment object {'name': 'projects/continual-test-proj/environments/staging',
            'summary': {'feature_set_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'model_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'feature_set_count': 0, 'feature_set_row_count': '0', 'feature_set_bytes': '0', 'feature_count': 0,
            'connection_count': 0, 'model_count': 0, 'model_version_count': 0, 'experiment_count': '0',
            'prediction_count': '0', 'run_count': '0', 'dataset_count': '0', 'dataset_version_count': '0'},
            'update_time': '2023-03-21T21:20:14.599457Z', 'create_time': '2023-03-21T21:20:14.599457Z',
            'source': '', 'env_type': '', 'is_protected': False, 'is_ephemeral': False}>
        """
        req = management_pb2.CreateEnvironmentRequest(
            parent=self.parent,
            environment=Environment(
                source=source,
                is_protected=is_protected,
                is_ephemeral=is_ephemeral,
                env_type=env_type,
                current_run=self.run_name,
            ).to_proto(),
            environment_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateEnvironment(req)
        return Environment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def name(self, id: str, parent: Optional[str] = None) -> str:
        """Get the fully qualified name of this environment.

        Arguments:
            id: The environment id.
            parent: The parent project name.

        Return:
            string name of the environment.
        """
        if "/" in id:
            # Don't allow names to override manager parent config since this is confusing
            # and is typically a bug in the user code.
            if parent is not None and parent != "" and not id.startswith(parent):
                raise ValueError(f"Resource {id} not a child of {parent}.")
            return id

        name_str = self.parent or ""
        name_str += "/environments/" + id
        return name_str

    def get(self, id: str = "production") -> Environment:
        """Get environment.

        Arguments:
            id: environment name or id.

        Returns
            A environment.

        Examples:
            >>> # project is a Project object
            >>> env = proj.environments.create(id="staging")
            >>> proj.environments.get(id=env.name)
            <Environment object {'name': 'projects/continual-test-proj/environments/staging',
            'summary': {'feature_set_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'model_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'feature_set_count': 0, 'feature_set_row_count': '0', 'feature_set_bytes': '0', 'feature_count': 0,
            'connection_count': 0, 'model_count': 0, 'model_version_count': 0, 'experiment_count': '0',
            'prediction_count': '0', 'run_count': '0', 'dataset_count': '0', 'dataset_version_count': '0'},
            'update_time': '2023-03-21T21:20:14.599457Z', 'create_time': '2023-03-21T21:20:14.599457Z',
            'source': '', 'env_type': '', 'is_protected': False, 'is_ephemeral': False}>
        """
        req = management_pb2.GetEnvironmentRequest(name=self.name(id))
        resp = self.client._management.GetEnvironment(req)
        return Environment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        default_sort_order: str = "ASC",
    ) -> List[Environment]:
        """List environments.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of environments.

        Examples:
            >>> # project is a Project object
            >>> envs = [proj.environments.create(id=f"env{3-i}") for i in range(3)]
            >>> [env.id for env in proj.environments.list(page_size=10)]
            ['env2', 'env1', 'env0']
            >>> [env.id for env in proj.environments.list(page_size=3, order_by="id")]
            ['env0', 'env1', 'env2']
            >>> [env.id for env in proj.environments.list(page_size=3, order_by="id", default_sort_order="DESC")]
            ['env2', 'env1', 'env0']
        """
        req = management_pb2.ListEnvironmentsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListEnvironments(req)
        return [
            Environment.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.environments
        ]

    def list_all(self) -> Pager[Environment]:
        """List all environments.

        Pages through all environments using an iterator.

        Returns:
            A iterator of all environments.

        Examples:
            >>> # project is a Project object
            >>> envs = [proj.environments.create(id=f"env{3-i}") for i in range(3)]
            >>> [env.id for env in proj.environments.list_all()]
            ['env2', 'env1', 'env0']
        """

        def next_page(next_page_token):
            req = management_pb2.ListEnvironmentsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListEnvironments(req)
            return (
                [
                    Environment.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.environments
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def delete(
        self,
        id: str,
    ) -> None:
        """Delete an Environment.

        Arguments:
            id: Environment name or id.

        Examples:
            >>> # project is a Project object
            >>> env = proj.environments.create(id="example")
            >>> len(proj.environments.list_all())
            1
            >>> proj.environments.delete(id=env.name)
            >>> len(proj.environments.list_all())
            0
        """

        req = management_pb2.DeleteEnvironmentRequest(name=self.name(id))
        self.client._management.DeleteEnvironment(req)

    def update(
        self,
        paths: List[str],
        environment: Environment,
    ) -> Environment:
        """Update Environment.

        Arguments:
            paths: A list of paths to be updated.
            environment: Environment object containing updated fields.

        Returns:
            An updated Environment.

        Examples:
            >>> # project is a Project object
            >>> env = proj.environments.create(id="example")
            >>> env.env_type
            ''
            >>> env.env_type = "pre-production"
            >>> updated_env = proj.environments.update(paths=["env_type"], environment=env)
            >>> updated_env.env_type
            'pre-production'
        """

        req = management_pb2.UpdateEnvironmentRequest(
            environment=environment.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateEnvironment(req)
        return Environment.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class Environment(Resource, types.Environment):
    """Environment resource."""

    name_pattern: str = "projects/{project}/environments/{environment}"
    _manager: EnvironmentManager

    _models: ModelManager

    _datasets: DatasetManager

    _artifacts: ArtifactsManager

    _runs: RunManager

    def _init(self):
        self._manager = EnvironmentManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._models = ModelManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._datasets = DatasetManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._artifacts = ArtifactsManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )
        self._runs = RunManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def models(self) -> ModelManager:
        """Models manager."""
        return self._models

    @property
    def datasets(self) -> DatasetManager:
        """Datasets manager."""
        return self._datasets

    @property
    def artifacts(self) -> ArtifactsManager:
        """Artifacts manager."""
        return self._artifacts

    @property
    def runs(self) -> RunManager:
        """Runs manager."""
        return self._runs

    def delete(self) -> None:
        """Delete environment.

        Examples:
            >>> # project is a Project object
            >>> env = proj.environments.create(id="example")
            >>> len(proj.environments.list_all())
            1
            >>> env.delete()
            >>> len(proj.environments.list_all())
            0
        """
        self._manager.delete(self.name)

    def update(self, paths: List[str]) -> Environment:
        """Update Environment.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Environment.

        Examples:
            >>> # project is a Project object
            >>> env = proj.environments.create(id="example")
            >>> env.env_type
            ''
            >>> env.env_type = "pre-production"
            >>> updated_env = env.update(paths=["env_type"])
            >>> updated_env.env_type
            'pre-production'
        """
        return self._manager.update(paths=paths, environment=self)
