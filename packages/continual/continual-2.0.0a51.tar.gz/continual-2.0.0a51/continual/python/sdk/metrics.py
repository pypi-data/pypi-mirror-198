from __future__ import annotations
from typing import List, Optional, Any, Union
from datetime import datetime

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager


class MetricsManager(Manager):
    """Manages metric resources."""

    # the name pattern for metrics depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        id: str,
        display_name: str = "",
        direction: str = "UNSPECIFIED",
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> Metric:
        """Create a Metric.

        Arguments:
            id: identifier for the metric (e.g. `"accuracy"`)
            display_name: the display name of the metric
            direction: direction of the metric (e.g. `"HIGHER"`, `"LOWER"`, or `"UNSPECIFIED"`)
            tags: a dict of tags to add to this metric
            replace_if_exists: if the metric exists and this is true, update the current metric and return, else raise an error if the metric already exists

        Returns:
            A new metric.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> model_version.metrics.create(id="accuracy", display_name="Accuracy as percentage of correct predictions.", direction="HIGHER")
            <Metric object {'name': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgd2g225lsriq8gqsa50/metrics/accuracy',
            'display_name': 'Accuracy as percentage of correct predictions.', 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'create_time': '2023-03-21T23:23:56.378502Z', 'update_time': '2023-03-21T23:23:56.378502Z', 'direction': 'HIGHER',
            'created_by': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0', 'tags': {}}>
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        req = management_pb2.CreateMetricRequest(
            metric=Metric(
                display_name=display_name,
                direction=direction,
                run=self.run_name,
                tags=tags,
                current_run=self.run_name,
            ).to_proto(),
            metric_id=id,
            parent=self.parent,
            replace_if_exists=replace_if_exists,
        )

        resp = self.client._management.CreateMetric(req)
        return Metric.from_proto(resp, client=self.client, current_run=self.run_name)

    def log(
        self,
        metric_name: str,
        value: Any,
        group: str = "",
        timestamp: Union[str, datetime] = None,
        step: int = 0,
        label: str = "",
        replace_if_exists: bool = False,
    ):
        """Log a Metric Value.

        Arguments:
            metric_name: the name of the metric to log this value for
            value: value of the metric
            group: [Optional] name of the group to which this metric belongs (e.g. `"train"`)
            timestamp: [Optional] timestamp for which the value has been logged for
            step: [Optional] step at which the metric was logged, allows metrics to be grouped into a sequence
            label: [Optional] a label that describes the value
            replace_if_exists: if the metric value exists and this is true, update the current metric value and return, else raise an error if the metric value already exists

        Examples:
            >>> # model_version is a ModelVersion object and metric is a Metric object
            >>> metric = model_version.metrics.get("accuracy")
            >>> len(metric.values())
            0
            >>> model_version.metrics.log(metric_name=metric.name, value=0.9, group="train")
            >>> len(metric.values())
            1
            >>> metric.values()[0].value, metric.values()[0].group
            0.9, 'train'
            >>> [model_version.metrics.log(metric_name=metric.name, value=(i*1.0/10), group="train", step=i) for i in range(10)]
            >>> len(metric.values())
            11
        """
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        req = management_pb2.LogMetricRequest(
            parent=self.name(
                metric_name, self.parent, f"{self.parent}/metrics/{metric_name}"
            ),
            value=types.MetricValue(
                value=float(value) if isinstance(value, int) else value,
                group=group,
                step=step,
                timestamp=timestamp,
                run=self.run_name,
                label=label,
            ).to_proto(),
            replace_if_exists=replace_if_exists,
        )
        self.client._management.LogMetric(req)
        return

    def get(self, id: str) -> Metric:
        """Get metric.

        Arguments:
            id: Metric name or id

        Returns
            A Metric.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> [model_version.metrics.create(id=f"metric-{i}", direction="HIGHER") for i in range(3)]
            >>> model_version.metrics.get("metric-0")
            <Metric object {'name': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgd2g225lsriq8gqsa50/metrics/metric-0',
            'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og', 'create_time': '2023-03-21T23:38:50.592617Z',
            'update_time': '2023-03-21T23:38:50.592617Z', 'direction': 'HIGHER', 'created_by': 'projects/continual-test-proj/apikeys/cg9ptqa5lsruiddmj9v0',
            'display_name': '', 'tags': {}}>
        """
        req = management_pb2.GetMetricRequest(
            name=self.name(
                id=id,
                parent=self.parent,
                name_pattern=self.parent + "/metrics/{metric}",
            ),
        )
        metric = self.client._management.GetMetric(req)
        return Metric.from_proto(metric, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[Metric]:
        """List metrics.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of metrics.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> [model_version.metrics.create(id=name, direction="HIGHER") for name in ['precision', 'recall', 'f1-score']]
            >>> [m.id for m in model_version.metrics.list(page_size=5)]
            ['precision', 'recall', 'f1-score']
            >>> [m.id for m in model_version.metrics.list(page_size=10,order_by="id")]
            ['f1-score', 'precision', 'recall']
            >>> [m.id for m in model_version.metrics.list(page_size=10, order_by="id", default_sort_order="DESC")]
            ['recall', 'precision', 'f1-score']
        """
        req = management_pb2.ListMetricsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListMetrics(req)
        return [
            Metric.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.metrics
        ]

    def list_all(self) -> Pager[Metric]:
        """List all metrics.

        Pages through all metrics using an iterator.

        Returns:
            A iterator of all metrics.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> [model_version.metrics.create(id=name, direction="HIGHER") for name in ['precision', 'recall', 'f1-score']]
            >>> [m.id for m in model_version.metrics.list_all()]
            ['precision', 'recall', 'f1-score']
        """

        def next_page(next_page_token):
            req = management_pb2.ListMetricsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListMetrics(req)
            return (
                [
                    Metric.from_proto(x, client=self.client, current_run=self.run_name)
                    for x in resp.metrics
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        metric: Metric,
    ) -> Metric:
        """Update Metric.

        Arguments:
            paths: A list of paths to be updated.
            metric: Metric object containing updated fields.

        Returns:
            An updated Metric.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metric = model_version.metrics.create(id="metric-0", direction="HIGHER")
            >>> metric.direction
            'HIGHER'
            >>> metric.direction = "LOWER"
            >>> updated_metric = model_version.metrics.update(paths=["direction"], metric=metric)
            >>> updated_metric.direction
            'LOWER'
        """

        req = management_pb2.UpdateMetricRequest(
            metric=metric.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateMetric(req)
        return Metric.from_proto(resp, client=self.client, current_run=self.run_name)

    def values(
        self,
        id: str = None,
        page_size: Optional[int] = 0,
        filters: List[str] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[types.MetricValue]:
        """List metric values for the metric with the given id.

        Arguments:
            id: The id of the metric to list values for.
            page_size: Number of items to return.
            filters: A list of filters to be applied to the metric values.
            order_by: A comma-separated list of fields to order by, sorted in default order. Use "desc" after a field name for descending.
            default_sort_order: The default sort order for the list.

        Returns:
            A list of metric values.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metric = model_version.metrics.create(id="example-metric", direction="HIGHER")
            >>> [metric.log(value=19 - (1.0 * i),group=f"test-{i//2}",step=i) for i in range(20)]
            >>> [v.values for model_version.metrics.values(id=metric.id, page_size=20)]
            [19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
            >>> [v.step for v in model_version.metrics.values(id=metric.id, page_size=20, order_by="group_name, step desc")]
            [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
            >>> [v.value for v in model_version.metrics.values(id=metric.id, page_size=20, filters=["group_name:test-0"])]
            [19.0, 18.0]
        """

        req = management_pb2.ListMetricValuesRequest(
            parent=self.name(
                id=id,
                parent=self.parent,
                name_pattern=self.parent + "/metrics/{metric}",
            ),
            page_size=page_size,
            filters=filters,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListMetricValues(req)
        return [
            types.MetricValue.from_proto(
                x, client=self.client, current_run=self.run_name
            )
            for x in resp.metric_values
        ]


class Metric(Resource, types.Metric):
    """Metric resource."""

    # the name pattern for metrics depends on the resource it was created for
    name_pattern: str = ""

    _manager: MetricsManager
    """Metrics manager."""

    def _init(self):
        self._manager = MetricsManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )

    def log(
        self,
        value: Any,
        group: str = "",
        timestamp: Union[str, datetime] = None,
        step: int = 0,
        label: str = "",
        replace_if_exists: bool = False,
    ):
        """Log a Metric Value for the current Metric.

        Arguments:
            value: value of the metric
            group: [Optional] name of the group to which this metric belongs (e.g. `"train"`)
            timestamp: [Optional] timestamp for which the value has been logged for
            step: [Optional] step at which the metric was logged, allows metrics to be grouped into a sequence
            label: [Optional] a label that describes the value
            replace_if_exists: if the metric value exists and this is true, update the current metric value and return, else raise an error if the metric value already exists

        Returns:

        Examples:
            >>> # model_version is a ModelVersion object and metric is a Metric object
            >>> metric = model_version.metrics.get("accuracy")
            >>> len(metric.values())
            0
            >>> metric.log(metric_name=metric.name, value=0.9, group="train")
            >>> len(metric.values())
            1
            >>> metric.values()[0].value, metric.values()[0].group
            0.9, 'train'
            >>> [metric.log(metric_name=metric.name, value=(i*1.0/10), group="train", step=i) for i in range(10)]
            >>> len(metric.values())
            11
        """
        self._manager.log(
            metric_name=self.name,
            value=value,
            group=group,
            step=step,
            timestamp=timestamp,
            label=label,
            replace_if_exists=replace_if_exists,
        )

    def update(self, paths: List[str]) -> Metric:
        """Update Metric.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Metric.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metric = model_version.metrics.create(id="metric-0", direction="HIGHER")
            >>> metric.direction
            'HIGHER'
            >>> metric.direction = "LOWER"
            >>> updated_metric = metric.update(paths=["direction"])
            >>> updated_metric.direction
            'LOWER'
        """
        return self._manager.update(paths=paths, metric=self)

    def add_tags(self, tags: dict[str, str]) -> Metric:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Metric.

        Examples:
            >>> # metric is a Metric object with tags {"color": "red"}
            >>> metric.tags
            {'color': 'red'}
            >>> updated_metric = metric.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_metric.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(metric=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Metric:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Metric.

        Examples:
            >>> # metric is a Metric object with tags {"color": "red"}
            >>> metric.tags
            {'color': 'red'}
            >>> updated_metric = metric.remove_tags(["color", "fruit"])
            >>> updated_metric.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(metric=self, paths=["tags"])

    def values(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[types.MetricValue]:
        """List metric values for this metric.

        Arguments:
            page_size: [Optional] The maximum number of metric values to return. If unspecified, the server will pick an appropriate default.
            filters: [Optional] A list of filters to apply. Only metric values that match all of the specified filters will be returned.
            order_by: [Optional] A comma-separated list of fields to order by, sorted in default order. Use "desc" after a field name for descending.
            default_sort_order: [Optional] The default sort order for results. If not specified, "asc" is used.

        Returns:
            A list of MetricValue objects.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metric = model_version.metrics.create(id="example-metric", direction="HIGHER")
            >>> [metric.log(value=19 - (1.0 * i),group=f"test-{i//2}",step=i) for i in range(20)]
            >>> [v.values for metric.values(page_size=20)]
            [19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
            >>> [v.step for v in metric.values(page_size=20, order_by="group_name, step desc")]
            [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
            >>> [v.value for v in metric.values(page_size=20, filters=["group_name:test-0"])]
            [19.0, 18.0]
        """

        return self._manager.values(
            id=self.name,
            page_size=page_size,
            filters=filters,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )

    def latest_value(self, group: Optional[str] = None) -> types.MetricValue:
        """Gets the latest metric value.

        Arguments:
            group: [Optional] The group to get the latest metric value for. If not specified, the latest metric value for all groups will be returned.

        Returns:
            The latest MetricValue.

        Examples:
            >>> # model_version is a ModelVersion object
            >>> metric = model_version.metrics.create(id="example-metric", direction="HIGHER")
            >>> [metric.log(value=19 - (1.0 * i),group=f"test-{i//2}",step=i) for i in range(20)]
            >>> metric.latest_value().value
            0.0
            >>> metric.latest_value().step
            19
            >>> metric.latest_value(group="test-0").value
            18.0
            >>> metric.latest_value(group="test-5").step
            11
        """
        if group:
            return self.values(
                page_size=1, filters=[f"group_name:{group}"], default_sort_order="DESC"
            )[-1]
        else:
            return self.values(page_size=1, default_sort_order="DESC")[-1]
