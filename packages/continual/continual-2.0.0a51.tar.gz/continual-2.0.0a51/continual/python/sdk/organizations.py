from __future__ import annotations
from typing import List, Optional
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.projects import ProjectManager


class OrganizationManager(Manager):
    """Manages user resources."""

    name_pattern: str = "organizations/{user}"

    def create(
        self,
        display_name: str,
        tags: Optional[dict[str, str]] = None,
    ) -> Organization:
        """Create an organization.

        Arguments:
            display_name: Display name.
            tags: Tags to add to the organization.

        Returns:
            A new organization.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> client.organizations.create(display_name="example-org")
            <Organization object {'name': 'organizations/ced8rci5lsrrfj0t5f30', 'display_name': 'example-org',
            'update_time': '2022-12-15T03:00:02.419421Z', 'create_time': '2022-12-15T03:00:02.419421Z',
            'status': 'EXPIRED', 'trial_credits': '0', 'trial_credits_used': '0', 'show_plan': False,
            'sso_enabled': False, 'requires_sso': False, 'sso_domains': [], 'allow_external_users': False,
            'sso_configured': False, 'directory_sync_configured': False}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateOrganizationRequest(
            organization=types.Organization(
                display_name=display_name, tags=tags, current_run=self.run_name
            ).to_proto()
        )
        resp = self.client._management.CreateOrganization(req)
        return Organization.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def get(self, id: str) -> Organization:
        """Get organization.

        Arguments:
            id: Organization name or id.

        Returns
            An organization.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> org = client.organizations.create(display_name="example-org")
            >>> client.organizations.get(id=org.name)
            <Organization object {'name': 'organizations/ced8rci5lsrrfj0t5f30', 'display_name': 'example-org',
            'update_time': '2022-12-15T03:00:02.419421Z', 'create_time': '2022-12-15T03:00:02.419421Z',
            'status': 'EXPIRED', 'trial_credits': '0', 'trial_credits_used': '0', 'show_plan': False,
            'sso_enabled': False, 'requires_sso': False, 'sso_domains': [], 'allow_external_users': False,
            'sso_configured': False, 'directory_sync_configured': False}>
        """
        req = management_pb2.GetOrganizationRequest(name=self.name(id))
        resp = self.client._management.GetOrganization(req)
        return Organization.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        default_sort_order: str = "ASC",
    ) -> List[Organization]:
        """List organizations.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Organizations.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> orgs = [client.organizations.create(display_name=f"example-org-{5-i}") for i in range(5)]
            >>> [org.display_name for org in client.organizations.list(page_size=10)] # Orders by 'create_time' by default
            ['example-org-5', 'example-org-4', 'example-org-3', 'example-org-2', 'example-org-1']
            >>> [org.display_name for org in client.organizations.list(page_size=10, order_by="display_name")]
            ['example-org-1', 'example-org-2', 'example-org-3', 'example-org-4', 'example-org-5']
            >>> [org.display_name for org in client.organizations.list(page_size=10, order_by="display_name", default_sort_order="DESC")]
            ['example-org-5', 'example-org-4', 'example-org-3', 'example-org-2', 'example-org-1']
        """
        req = management_pb2.ListOrganizationsRequest(
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListOrganizations(req)
        return [
            Organization.from_proto(u, client=self.client, current_run=self.run_name)
            for u in resp.organizations
        ]

    def list_all(self) -> Pager[Organization]:
        """List all organizations.

        Pages through all organization using an iterator.

        Returns:
            A iterator of all organizations.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> orgs = [client.organizations.create(display_name=f"example-org-{i}") for i in range(10)]
            >>> [org.display_name for org in client.organizations.list_all()] # Orders by 'create_time' by default
            ['example-org-0', 'example-org-1', 'example-org-2', 'example-org-3', 'example-org-4', 'example-org-5',
            'example-org-6', 'example-org-7', 'example-org-8', 'example-org-9']
        """

        def next_page(next_page_token):
            req = management_pb2.ListOrganizationsRequest(page_token=next_page_token)
            resp = self.client._management.ListOrganizations(req)
            return (
                [
                    Organization.from_proto(
                        u, client=self.client, current_run=self.run_name
                    )
                    for u in resp.organizations
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def delete(self, id: str) -> None:
        """Delete an organization.

        Arguments:
            id: Organization name or id.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> orgs = [client.organizations.create(display_name=f"example-org-{i}") for i in range(10)]
            >>> [client.organizations.delete(id=org.id)  for org in client.organizations.list_all()]
            [None, None, None, None, None, None, None, None, None, None]
            >>> len([org  for org in client.organizations.list_all()])
            0
        """
        req = management_pb2.DeleteOrganizationRequest(name=self.name(id))
        self.client._management.DeleteOrganization(req)

    def update(
        self,
        paths: List[str],
        organization: Organization,
    ) -> Organization:
        """Update Organization.

        Arguments:
            paths: A list of paths to be updated.
            organization: Organization object containing updated fields.

        Returns:
            An updated Organization.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> org = client.organizations.create(display_name="name_wiht_typo")
            >>> org.display_name = "name_without_typo"
            >>> updated_org = client.organizations.update(organization=org, paths=["display_name"]])
            >>> updated_org.display_name
            'name_without_typo'
        """

        req = management_pb2.UpdateOrganizationRequest(
            organization=organization.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateOrganization(req)
        return Organization.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class Organization(Resource, types.Organization):
    """Organization resource."""

    name_pattern = "organizations/{users}"

    _manager: OrganizationManager

    _projects: ProjectManager

    def _init(self):
        self._manager = OrganizationManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._projects = ProjectManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def projects(self) -> ProjectManager:
        """Organization's Project Manager."""
        return self._projects

    def delete(self) -> None:
        """Delete organization.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> org = client.organizations.create(display_name="example-org")
            >>> org.delete()
            >>> len([org for org in client.organizations.list_all()])
            0
        """
        self._manager.delete(self.name)

    def update(
        self,
        paths: List[str] = None,
    ) -> Organization:
        """Update organization.

        Arguments:
            display_name:  Display name.

        Returns:
            Updated organization.

        Examples:
            >>> from continual import Client
            >>> client = Client() # Assuming credentials in YAML config
            >>> org = client.organizations.create(display_name="name_wiht_typo")
            >>> org.display_name = "name_without_typo"
            >>> updated_org = org.update(paths=["display_name"]])
            >>> updated_org.display_name
            'name_without_typo'
        """
        return self._manager.update(organization=self, paths=paths)

    def _create_user_role(self, user_name: str, role: str) -> None:
        """Create an organization role for a user

        Arguments:
            user_name: the name of the user
            role: the name of the role
        """

        req = management_pb2.CreateAccessPolicyRequest(
            parent=self.name,
            access_policy=types.AccessPolicy(
                resource=self.name, subject=user_name, role=role
            ).to_proto(),
        )
        self._manager.client._management.CreateAccessPolicy(req)

    def add_tags(self, tags: dict[str, str]) -> Organization:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Organization.

        Examples:
            >>> # organization is a Organization object with tags {"color": "red"}
            >>> organization.tags
            {'color': 'red'}
            >>> updated_organization = organization.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_organization.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(organization=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Organization:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Organization.

        Examples:
            >>> # organization is a Organization object with tags {"color": "red"}
            >>> organization.tags
            {'color': 'red'}
            >>> updated_organization = organization.remove_tags(["color", "fruit"])
            >>> updated_organization.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(organization=self, paths=["tags"])
