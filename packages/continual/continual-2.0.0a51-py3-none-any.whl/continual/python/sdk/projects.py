from __future__ import annotations
from typing import List, Optional
from continual.python.sdk.environments import EnvironmentManager
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager


class ProjectManager(Manager):
    """Manages project resources."""

    name_pattern: str = "projects/{project}"

    def create(
        self,
        organization: str,
        id: Optional[str] = "",
        display_name: Optional[str] = "",
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: Optional[bool] = False,
        create_source: Optional[str] = None,
        create_source_type: Optional[str] = types.ProjectCreateSourceType.NONE,
    ) -> Project:
        """Create an project.

        New projects are identified by a unique project id that is
        generated from the display name. However project ids are globally unique across
        all organizations.

        Arguments:
            organization: Organization resource name.
            display_name: Display name.
            id : Project id.
            tags: Tags to add to the project.
            replace_if_exists: If true, replace the project if it already exists.
            create_source: The source of the project creation.
            create_source_type: The type of the source of the project creation.

        Returns:
            A new project.

        Examples:
            >>> # org is an Organization object and client is a Client object
            >>> client.projects.create(display_name="example-proj", organization=org.name)
            <Project object {'name': 'projects/example-proj', 'display_name': 'example-proj',
            'organization': 'organizations/cg9on525lsruiddmj9gg', 'summary': {'model_count': 2, 'model_version_count': 5,
            'feature_set_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'model_health': {'healthy_count': 2, 'unhealthy_count': 0, 'critical_count': 0},
            'last_training_time': '2023-03-22T01:37:42.108358Z', 'run_count': '5', 'dataset_count': '15',
            'dataset_version_count': '23', 'feature_set_count': 0, 'feature_set_row_count': '0', 'feature_set_bytes': '0',
            'feature_count': 0, 'connection_count': 0, 'experiment_count': '0', 'prediction_count': '0'},
            'update_time': '2023-03-22T05:37:14.640761Z', 'create_time': '2023-03-16T21:35:19.766855Z',
            'default_environment': 'projects/example-proj/environments/production', 'create_source_type': 'NONE',
            'create_source': '', 'git_integration': '', 'tags': {}}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateProjectRequest(
            project=Project(
                display_name=display_name,
                organization=organization,
                tags=tags,
                current_run=self.run_name,
                create_source=create_source,
                create_source_type=create_source_type,
            ).to_proto(),
            project_id=id,
            replace_if_exists=replace_if_exists,
        )

        resp = self.client._management.CreateProject(req)
        return Project.from_proto(resp, client=self.client, current_run=self.run_name)

    def get(self, id: str) -> Project:
        """Get project.

        Arguments:
            id: Project name or id.

        Returns
            A project.

        Examples:
            >>> # org is an Organization object and client is a Client object
            >>> proj = client.projects.create(display_name="example-proj", organization=org.name)
            >>> client.projects.get(proj.name)
            <Project object {'name': 'projects/example-proj', 'display_name': 'example-proj',
            'organization': 'organizations/cg9on525lsruiddmj9gg', 'summary': {'model_count': 2, 'model_version_count': 5,
            'feature_set_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'model_health': {'healthy_count': 2, 'unhealthy_count': 0, 'critical_count': 0},
            'last_training_time': '2023-03-22T01:37:42.108358Z', 'run_count': '5', 'dataset_count': '15',
            'dataset_version_count': '23', 'feature_set_count': 0, 'feature_set_row_count': '0', 'feature_set_bytes': '0',
            'feature_count': 0, 'connection_count': 0, 'experiment_count': '0', 'prediction_count': '0'},
            'update_time': '2023-03-22T05:37:14.640761Z', 'create_time': '2023-03-16T21:35:19.766855Z',
            'default_environment': 'projects/example-proj/environments/production', 'create_source_type': 'NONE',
            'create_source': '', 'git_integration': '', 'tags': {}}>
            >>> client.projects.get("example-proj")
            <Project object {'name': 'projects/example-proj', 'display_name': 'example-proj',
            'organization': 'organizations/cg9on525lsruiddmj9gg', 'summary': {'model_count': 2, 'model_version_count': 5,
            'feature_set_health': {'healthy_count': 0, 'unhealthy_count': 0, 'critical_count': 0},
            'model_health': {'healthy_count': 2, 'unhealthy_count': 0, 'critical_count': 0},
            'last_training_time': '2023-03-22T01:37:42.108358Z', 'run_count': '5', 'dataset_count': '15',
            'dataset_version_count': '23', 'feature_set_count': 0, 'feature_set_row_count': '0', 'feature_set_bytes': '0',
            'feature_count': 0, 'connection_count': 0, 'experiment_count': '0', 'prediction_count': '0'},
            'update_time': '2023-03-22T05:37:14.640761Z', 'create_time': '2023-03-16T21:35:19.766855Z',
            'default_environment': 'projects/example-proj/environments/production', 'create_source_type': 'NONE',
            'create_source': '', 'git_integration': '', 'tags': {}}>
        """

        req = management_pb2.GetProjectRequest(name=self.name(id))
        resp = self.client._management.GetProject(req)
        return Project.from_proto(resp, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        default_sort_order: str = "ASC",
    ) -> List[Project]:
        """List projects.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Projects.

        Examples:
            >>> # org is an Organization object and client is a Client object
            >>> org = client.organizations.create(display_name="example-org")
            >>> projs = [client.projects.create(id=f"project-{i}", display_name="Rank {10-i} project", organization=org.name) for i in range(10)]
            >>> [c.id for client.projects.list(page_size=10)]
            ['project-0', 'project-1', 'project-2', 'project-3', 'project-4', 'project-5', 'project-6', 'project-7', 'project-8', 'project-9']
            >>> [c.id for client.projects.list(page_size=10, order_by="display_name")]
            ['project-9', 'project-8', 'project-7', 'project-6', 'project-5', 'project-4', 'project-3', 'project-2', 'project-1', 'project-0']
            >>> [c.id for client.projects.list(page_size=10, order_by="display_name", default_sort_order="DESC")]
            ['project-0', 'project-1', 'project-2', 'project-3', 'project-4', 'project-5', 'project-6', 'project-7', 'project-8', 'project-9']
        """

        req = management_pb2.ListProjectsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListProjects(req)
        return [
            Project.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.projects
        ]

    def list_all(self) -> Pager[Project]:
        """List all projects.

        Pages through all projects using an iterator.

        Returns:
            A iterator of all projects.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> org = client.organizations.create(display_name="example-org")
            >>> projs = [client.projects.create(id=f"project-{i}", organization=org.name) for i in range(5)]
            >>> [c.id for client.projects.list_all()]
            ['project-0', 'project-1', 'project-2', 'project-3', 'project-4']
        """

        def next_page(next_page_token):
            req = management_pb2.ListProjectsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListProjects(req)
            return (
                [
                    Project.from_proto(x, client=self.client, current_run=self.run_name)
                    for x in resp.projects
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def delete(self, id: str) -> None:
        """Delete an project.

        Arguments:
            id: Project name or id.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> org = client.organizations.create(display_name="example-org")
            >>> projs = [client.projects.create(display_name=f"project-{i}", organization=org.id) for i in range(10)]
            >>> [client.projects.delete(id=proj.id)  for proj in client.projects.list_all()]
            [None, None, None, None, None, None, None, None, None, None]
            >>> len([org  for org in client.projects.list_all()])
            0
        """

        req = management_pb2.DeleteProjectRequest(name=self.name(id))
        self.client._management.DeleteProject(req)

    def update(
        self,
        paths: List[str],
        project: Project,
    ) -> Project:
        """Update Project.

        Arguments:
            paths: A list of paths to be updated.
            project: Project object containing updated fields.

        Returns:
            An updated Project.

        Examples:
            >>> # org is an Organization object and client is a Client object
            >>> proj = client.projects.create(display_name="example-proj", organization=org.name)
            >>> proj.display_name
            'example-proj'
            >>> proj.display_name = "updated-example-proj"
            >>> proj = client.projects.update(paths=["display_name"], project=proj)
            >>> proj.display_name
            'updated-example-proj'
        """
        req = management_pb2.UpdateProjectRequest(
            project=project.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateProject(req)
        return Project.from_proto(resp, client=self.client, current_run=self.run_name)


class Project(Resource, types.Project):
    """Project resource."""

    name_pattern: str = "projects/{project}"

    _manager: ProjectManager

    _environments: EnvironmentManager

    def _init(self):
        self._manager = ProjectManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._environments = EnvironmentManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def environments(self) -> EnvironmentManager:
        """Environments manager."""
        return self._environments

    def delete(self) -> None:
        """Delete project.

        Examples:
            >>> # proj is a Project object and client is a Client object
            >>> len([proj for proj in client.projects.list_all()])
            1
            >>> proj.delete()
            >>> len([proj for proj in client.projects.list_all()])
            0
        """
        self._manager.delete(self.name)

    def update(self, paths: List[str] = None) -> Project:
        """Update project.

        Arguments:
            paths: A list of paths to be updated

        Returns:
            Updated project.

        Examples:
            >>> # org is an Organization object and client is a Client object
            >>> proj = client.projects.create(display_name="example-proj", organization=org.name)
            >>> proj.display_name
            'example-proj'
            >>> proj.display_name = "updated-example-proj"
            >>> updated_proj = proj.update(paths=["display_name"], project=proj)
            >>> updated_oroj.display_name
            'updated-example-proj'
        """
        return self._manager.update(project=self, paths=paths)

    def add_tags(self, tags: dict[str, str]) -> Project:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Project.

        Examples:
            >>> # project is a Project object with tags {"color": "red"}
            >>> project.tags
            {'color': 'red'}
            >>> updated_project = project.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_project.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(project=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Project:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Project.

        Examples:
            >>> # project is a Project object with tags {"color": "red"}
            >>> project.tags
            {'color': 'red'}
            >>> updated_project = project.remove_tags(["color", "fruit"])
            >>> updated_project.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(project=self, paths=["tags"])
