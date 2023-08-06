from __future__ import annotations
from typing import List, Optional, Any

from continual.python.sdk.iterators import Pager
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.rpc.management.v1 import (
    management_pb2,
    types as management_types_py,
)
import json
import numpy as np
import datetime


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        try:
            x = str(obj)
        except:
            pass
        else:
            return x
        return json.JSONEncoder.default(self, obj)


class MetadataManager(Manager):
    """Manages metadata resources."""

    # the name pattern for metadata depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        id: str = "",
        data: dict = None,
        replace_if_exists: bool = False,
    ) -> Metadata:
        """Create metadata.

        Arguments:
            id: A common name used to retrieve the metadata
            data: the metadata
            replace_if_exists: If true, update the metadata if it already exists

        Returns
            A Metadata object

        Examples:
            >>> # model_version is a ModelVersion object
            >>> model_version.metadata.create(
            ...      id="test-map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ... )
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cesbtva5lsrmkt2jtbe0/metadata/test-map',
            'create_time': '2023-01-07T00:38:21.965768Z', 'update_time': '2023-01-07T00:38:21.965768Z', 'data': '{"key1": "value1", "key2": 10, "key3": 0.5}',
            'run': 'projects/continual_test_proj/environments/production/runs/cesceta5lsrkagaitff0'}>
            >>> model_version.metadata.create(
            ...     data={"key1": "value1", "key2": 10, "key3": 0.5},
            ... )
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cesceta5lsrkagaitfh0/metadata/ceschiq5lsrkagaitfj0',
            'run': 'projects/continual_test_proj/environments/production/runs/cesceta5lsrkagaitff0', 'create_time': '2023-01-07T01:20:11.541916Z',
            'update_time': '2023-01-07T01:20:11.541916Z', 'data': '{"key1": "value1", "key2": 10, "key3": 0.5}'}>
            >>> model_version.metadata.create(
            ...     id="test-map",
            ...     data={"key1": "value2", "key2": 10, "key3": 0.5},
            ...     replace_if_exists=True,
            ... )
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cesbtva5lsrmkt2jtbe0/metadata/test-map',
            'create_time': '2023-01-07T00:38:21.965768Z', 'update_time': '2023-01-07T00:38:21.965768Z', 'data': '{"key1": "value2", "key2": 10, "key3": 0.5}',
            'run': 'projects/continual_test_proj/environments/production/runs/cesceta5lsrkagaitff0'}>
        """

        req = management_pb2.CreateMetadataRequest(
            parent=self.parent,
            metadata=Metadata(
                run=self.run_name,
                data=json.dumps(data, cls=NpEncoder),
                current_run=self.run_name,
            ).to_proto(),
            metadata_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateMetadata(req)
        return Metadata.from_proto(resp, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[Metadata]:
        """List metadata.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Metadata.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metadatas = [model_version.metadata.create(id=f"md-{i}", data={"key1": f"value{3-i}"}) for i in range(3)]
            >>> [m.id for m in model_version.metadata.list(page_size=5)]
            ['md-0', 'md-1', 'md-2']
            >>> [m.id for m in model_version.metadata.list(page_size=5, order_by="data desc")]
            ['md-2', 'md-1', 'md-0']
            >>> [m.id for m in model_version.metadata.list(page_size=5, default_sort_order="DESC")]
            ['md-0', 'md-1', 'md-2']
        """
        if not self.client:
            print(f"Cannot list metadata without client")
            return

        req = management_pb2.ListMetadataRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListMetadata(req)
        return [
            Metadata.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.metadata
        ]

    def list_all(self) -> Pager[Metadata]:
        """List all metadata.

        Pages through all metadata using an iterator.

        Returns:
            A iterator of all metadata.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metadatas = [model_version.metadata.create(id=f"md-{i}", data={"key1": f"value{3-i}"}) for i in range(5)]
            >>> [m.data['key1'] for m in model_version.metadata.list_all()]
            ['value3', 'value2', 'value1', 'value0', 'value-1']
        """

        def next_page(next_page_token):
            req = management_pb2.ListMetadataRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListMetadata(req)
            return (
                [
                    Metadata.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.metadata
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def get(self, id: str = "") -> Metadata:
        """Get metadata.

        Arguments:
            id: Fully qualified name or id for the metadata.

        Return
            Metadata

        Examples:
            >>> # model_version is a ModelVersion object
            >>> md = model_version.metadata.create(
            ...      id="test-map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ... )
            >>> model_version.metadata.get("test-map")
            <Metadata object {'name': 'projects/continual_test_proj/environments/production/models/test_model/versions/cesbtva5lsrmkt2jtbe0/metadata/test-map',
            'create_time': '2023-01-07T00:38:21.965768Z', 'update_time': '2023-01-07T00:38:21.965768Z', 'data': '{"key1": "value1", "key2": 10, "key3": 0.5}',
            'run': 'projects/continual_test_proj/environments/production/runs/cesceta5lsrkagaitff0'}>
        """
        if not self.client:
            print(f"Cannot fetch metadata without client")
            return

        req = management_pb2.GetMetadataRequest(
            name=self.name(id, self.parent, f"{self.parent}/metadata/{id}")
        )
        res = self.client._management.GetMetadata(req)
        return Metadata.from_proto(res, client=self.client, current_run=self.run_name)

    def delete(self, id: str):
        """Delete metadata.

        Arguments:
            id: The id or fully qualified name of the metadata obj

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metadata = model_version.metadata.create(
            ...      id="test-map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ... )
            >>> len(list(model_version.metadata.list_all()))
            1
            >>> model_version.metadata.delete(name=metadata.name)
            >>> len(list(model_version.metadata.list_all()))
            0
        """
        if not self.client:
            print(f"Cannot delete metadata without client")
            return

        req = management_pb2.DeleteMetadataRequest(
            name=self.name(id, self.parent, f"{self.parent}/metadata/{id}")
        )
        self.client._management.DeleteMetadata(req)

    def update(
        self,
        paths: List[str],
        metadata: Metadata,
    ) -> Metadata:
        """Update Metadata.

        Arguments:
            paths: A list of paths to be updated.
            metadata: Metadata object containing updated fields.

        Returns:
            An updated Metadata.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metadata = model_version.metadata.create(
            ...      id="test-map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ... )
            >>> metadata.data['key1'], metadata.data['key2']
            ('value1', 10)
            >>> metadata.data['key2'] = 20
            >>> metadata.data['key1'] = 'value2'
            >>> new_metadata = model_version.metadata.update(
            ...     paths=["data"],
            ...     metadata=metadata,
            ... )
            >>> new_metadata.data['key1'], new_metadata.data['key2']
            ('value2', 20)
        """

        req = management_pb2.UpdateMetadataRequest(
            metadata=metadata.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateMetadata(req)
        return Metadata.from_proto(resp, client=self.client, current_run=self.run_name)


class Metadata(Resource, management_types_py.Metadata):
    """Metadata resource."""

    # the name pattern for metadata depends on the resource it was created for
    name_pattern: str = ""

    _manager: MetadataManager
    """Metadata manager."""

    def _init(self):
        self._manager = MetadataManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )

    @property
    def data(self) -> str:
        return json.loads(self._attributes["data"])

    @data.setter
    def data(self, value: Any) -> None:
        if isinstance(value, str):
            management_types_py._set_attribute(
                self._attributes,
                "Metadata",
                "data",
                value,
                str,
                "",
            )
        else:
            management_types_py._set_attribute(
                self._attributes,
                "Metadata",
                "data",
                json.dumps(value, cls=NpEncoder),
                str,
                "",
            )

    def update(self, paths: List[str]) -> Metadata:
        """Update Metadata.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Metadata.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metadata = model_version.metadata.create(
            ...      id="test-map",
            ...      data={"key1": "value1", "key2": 10, "key3": 0.5},
            ... )
            >>> metadata.data['key1'], metadata.data['key2']
            ('value1', 10)
            >>> metadata.data['key2'] = 20
            >>> metadata.data['key1'] = 'value2'
            >>> new_metadata = metadata.update(
            ...     paths=["data"],
            ... )
            >>> new_metadata.data['key1'], new_metadata.data['key2']
            ('value2', 20)
        """
        return self._manager.update(paths=paths, metadata=self)
