from __future__ import annotations
from typing import Iterator, List, Optional

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.checks import ChecksManager
from continual.python.sdk.metadata import MetadataManager
from continual.python.sdk.metrics import MetricsManager


class EndpointManager(Manager):
    """Manages Endpoint resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/endpoints/{endpoint}"

    def create(
        self,
        id: Optional[str] = None,
        model_version: Optional[str] = None,
        uri: Optional[str] = None,
        state: Optional[str] = "ACTIVE",
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> Endpoint:
        """Create an Endpoint.

        Arguments:
            id: Endpoint name or id.
            model_version: Name of the model version to use on the endpoint
            uri: URI of the endpoint
            state: State of the endpoint (one of 'ACTIVE' or 'INACTIVE')
            tags: A dict of tags to add to this endpoint.
            replace_if_exists: If true, update the existing endpoint if it exists, else throw an error.

        Returns
            An Endpoint.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> model.endpoints.create(
            ...    id="example-endpoint",
            ...    model_version=model_version.name,
            ...    uri="http//test-uri.com",
            ... )
            <Endpoint object {'name': 'projects/continual-test-proj/environments/production/models/example-model/endpoints/example-endpoint',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcukqa5lsriq8gqs9eg',
            'uri': 'http//test-uri.com', 'create_time': '2023-03-21T17:33:47.761709Z', 'update_time': '2023-03-21T17:33:47.761709Z',
            'signature': {'inputs': [], 'outputs': []}, 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'state': 'ACTIVE', 'tags': {}}>
            >>> model.endpoints.create(
            ...    id="example-endpoint",
            ...    model_version=model_version.name,
            ...    uri="http//dummy-uri.com",
            ...    state="INACTIVE",
            ... )
            <Endpoint object {'name': 'projects/continual-test-proj/environments/production/models/example-model/endpoints/example-endpoint',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcukqa5lsriq8gqs9eg',
            'uri': 'http//dummy-uri.com', 'create_time': '2023-03-21T17:33:47.761709Z', 'update_time': '2023-03-21T17:33:47.761709Z',
            'signature': {'inputs': [], 'outputs': []}, 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'state': 'INACTIVE', 'tags': {}}>
        """
        req = management_pb2.CreateEndpointRequest(
            parent=self.parent,
            endpoint=Endpoint(
                run=self.run_name,
                model_version=self.name(
                    model_version,
                    self.parent,
                    f"{self.parent}/versions/{id}",
                ),
                uri=uri,
                state=state,
                tags=tags,
                current_run=self.run_name,
            ).to_proto(),
            endpoint_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateEndpoint(req)
        return Endpoint.from_proto(resp, client=self.client, current_run=self.run_name)

    def get(self, id: str) -> Endpoint:
        """Get an Endpoint.

        Arguments:
            id: Endpoint name or id.

        Returns
            An Endpoint.

        Examples:
            >>> # model is a Model object
            >>> endpoint = model.endpoints.create(
            ...    id="example-endpoint",
            ...    model_version=model_version.name,
            ...    uri="http//test-uri.com",
            ... )
            >>> model.endpoints.get("example-endpoint")
            <Endpoint object {'name': 'projects/continual-test-proj/environments/production/models/example-model/endpoints/example-endpoint',
            'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgcukqa5lsriq8gqs9eg',
            'uri': 'http//test-uri.com', 'create_time': '2023-03-21T17:33:47.761709Z', 'update_time': '2023-03-21T17:33:47.761709Z',
            'signature': {'inputs': [], 'outputs': []}, 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'state': 'ACTIVE', 'tags': {}}>
        """
        req = management_pb2.GetEndpointRequest(name=self.name(id))
        resp = self.client._management.GetEndpoint(req)
        return Endpoint.from_proto(resp, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        default_sort_order: str = "ASC",
        order_by: Optional[str] = None,
    ) -> List[Endpoint]:
        """List Endpoints.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Endpoints.

        Examples:
            >>> # model is a Model object
            >>> endpoints = [model.endpoints.create(id=f'mirror-{i}', model_version=model_version.name, uri='http//test-uri-{i}.com') for i in range(10)]
            >>> [e.id for e in model.endpoints.list(page_size=20)]
            ['mirror-0', 'mirror-1', 'mirror-2', 'mirror-3', 'mirror-4', 'mirror-5', 'mirror-6', 'mirror-7', 'mirror-8', 'mirror-9']
            >>> [e.id for e in model.endpoints.list(page_size=20, order_by="id", default_sort_order="DESC")]
            ['mirror-9', 'mirror-8', 'mirror-7', 'mirror-6', 'mirror-5', 'mirror-4', 'mirror-3', 'mirror-2', 'mirror-1', 'mirror-0']
            >>> [e.id for e in model.endpoints.list(page_size=20, order_by="id desc")]
            ['mirror-9', 'mirror-8', 'mirror-7', 'mirror-6', 'mirror-5', 'mirror-4', 'mirror-3', 'mirror-2', 'mirror-1', 'mirror-0']
        """
        req = management_pb2.ListEndpointsRequest(
            parent=self.parent,
            default_sort_order=default_sort_order,
            order_by=order_by,
            page_size=page_size,
        )
        resp = self.client._management.ListEndpoints(req)
        return [
            Endpoint.from_proto(u, client=self.client, current_run=self.run_name)
            for u in resp.endpoints
        ]

    def list_all(self) -> Iterator[Endpoint]:
        """List all Endpoints.

        Pages through all Endpoint using an iterator.

        Returns:
            A iterator of all Endpoint.

        Examples:
            >>> # model is a Model object
            >>> endpoints = [model.endpoints.create(id=f'mirror-{i}', model_version=model_version.name, uri='http//test-uri-{i}.com') for i in range(10)]
            >>> [e.id for e in model.endpoints.list_all()]
            ['mirror-0', 'mirror-1', 'mirror-2', 'mirror-3', 'mirror-4', 'mirror-5', 'mirror-6', 'mirror-7', 'mirror-8', 'mirror-9']
        """

        def next_page(next_page_token):
            req = management_pb2.ListEndpointsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListEndpoints(req)
            return (
                [
                    Endpoint.from_proto(
                        u, client=self.client, current_run=self.run_name
                    )
                    for u in resp.endpoints
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(self, endpoint: Endpoint, paths: List[str]) -> Endpoint:
        """Update an Endpoint.

        Arguments:
            endpoint: Endpoint object with updated fields.
            paths: List of fields to update.

        Returns
            An Endpoint.

        Examples:
            >>> # model is a Model object
            >>> endpoint = model.endpoints.create(
            ...    id="example-endpoint",
            ...    model_version=model_version.name,
            ...    uri="http//test-uri.com",
            ... )
            >>> endpoint.uri
            'http//test-uri.com'
            >>> endpoint.uri = "http//test-uri-2.com"
            >>> updated_endpoint = model.endpoints.update(endpoint=endpoint, paths=["uri"])
            >>> updated_endpoint.uri
            'http//test-uri-2.com'
        """
        req = management_pb2.UpdateEndpointRequest(
            endpoint=endpoint.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateEndpoint(req)
        return Endpoint.from_proto(resp, client=self.client, current_run=self.run_name)

    def delete(self, id: str):
        """Delete an Endpoint.

        Arguments:
            id: Endpoint name or id.

        Examples:
            >>> # model is a Model object
            >>> endpoint = model.endpoints.create(
            ...    id="example-endpoint",
            ...    model_version=model_version.name,
            ...    uri="http//test-uri.com",
            ... )
            >>> len(model.endpoints.list(page_size=20))
            1
            >>> model.endpoints.delete(id="example-endpoint")
            >>> len(model.endpoints.list(page_size=20))
            0
        """
        req = management_pb2.DeleteEndpointRequest(name=self.name(id))
        self.client._management.DeleteEndpoint(req)

    def _get_latest_endpoint(self) -> Endpoint:
        """Get latest endpoint.

        Returns:
            The most recently created Endpoint.

        Examples:
            >>> ...
        """
        req = management_pb2.GetLatestEndpointRequest(parent=self.parent)
        resp = self.client._management.GetLatestEndpoint(req)
        return Endpoint.from_proto(resp, client=self.client, current_run=self.run_name)


class Endpoint(Resource, types.Endpoint):
    """Endpoint resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/endpoints/{endpoint}"

    _manager: EndpointManager
    """Endpoint manager"""

    _metrics: MetricsManager
    """Metrics Manager"""

    _artifacts: ArtifactsManager
    """Artifacts Manager"""

    _metadata: MetadataManager
    """Metadata Manager"""

    _checks: ChecksManager

    def _init(self):
        self._manager = EndpointManager(
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

    def update(self, paths: List[str]) -> Endpoint:
        """Update Endpoint.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Endpoint.

        Examples:
            >>> # model is a Model object
            >>> endpoint = model.endpoints.create(
            ...    id="example-endpoint",
            ...    model_version=model_version.name,
            ...    uri="http//test-uri.com",
            ... )
            >>> endpoint.uri
            'http//test-uri.com'
            >>> endpoint.uri = "http//test-uri-2.com"
            >>> updated_endpoint = endpoint.update(paths=["uri"])
            >>> updated_endpoint.uri
            'http//test-uri-2.com'
        """
        return self._manager.update(paths=paths, endpoint=self)

    def add_tags(self, tags: dict[str, str]) -> Endpoint:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Endpoint.

        Examples:
            >>> # endpoint is a Endpoint object with tags {"color": "red"}
            >>> endpoint.tags
            {'color': 'red'}
            >>> updated_endpoint = endpoint.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_endpoint.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(endpoint=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Endpoint:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Endpoint.

        Examples:
            >>> # endpoint is a Endpoint object with tags {"color": "red"}
            >>> endpoint.tags
            {'color': 'red'}
            >>> updated_endpoint = endpoint.remove_tags(["color", "fruit"])
            >>> updated_endpoint.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(endpoint=self, paths=["tags"])
