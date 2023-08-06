from __future__ import annotations
from typing import List, Optional
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager

from continual.python.sdk.metadata import MetadataManager


class PromotionManager(Manager):
    """Manages promotion resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/promotions/{promotion}"

    def create(
        self,
        reason: str,
        model_version: str,
        improvement_metric: str,
        improvement_metric_value: float = 0.0,
        base_improvement_metric_value: float = 0.0,
        base_model_version: Optional[str] = None,
        id: Optional[str] = None,
        message: Optional[str] = None,
        tags: Optional[dict[str, str]] = None,
        replace_if_exists: bool = False,
    ) -> Promotion:
        """Create promotion.

        Arguments:
            reason: A description of why the model version is being promoted
            model_version: The name of the model_version
            improvement_metric: The name of the metric that was considered
            improvement_metric_value: The value of the metric that was considered if improved
            base_improvement_metric_value: The value of the metric that was improved upon
            id: Optional Promotion id.
            message: Optional Promotion message
            tags: Optional tags to be associated with the promotion.
            replace_if_exists: If True, will update the promotion if it already exists. If False, will throw an error if the promotion already exists.

        Returns:
            A Promotion.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> model.promotions.create(
            ...     id="example-promotion",
            ...     model_version=model_version.name,
            ...     reason="UPLIFT",
            ...     base_improvement_metric_value=0.8,
            ...     improvement_metric_value=0.9,
            ...     improvement_metric="accuracy",
            ...     tags={"test": "tag"},
            ... )
            <Promotion object {'name': 'projects/continual-test-proj/environments/production/models/example-model/promotions/example-promotion',
            'create_time': '2023-03-22T02:47:27.097419Z', 'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgd43u25lsriq8gqsamg',
            'improvement_metric': 'accuracy', 'improvement_metric_value': 0.9, 'base_improvement_metric_value': 0.8,
            'improvement_metric_diff': 0.09999999999999998, 'reason': 'UPLIFT', 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'tags': {'test': 'tag'}, 'base_model_version': '', 'message': '', 'account': ''}>
            >>> # Creating a promotion with the same id will throw an error
            >>> model.promotions.create(
            ...     id="example-promotion",
            ...     model_version=model_version.name,
            ...     reason="MANUAL",
            ...     base_improvement_metric_value=0.8,
            ...     improvement_metric_value=0.9,
            ...     improvement_metric="accuracy",
            ...     tags={"test": "tag2"},
            ... )
            Exception: ('Resource already exists.', {'name': 'projects/continual-test-proj/environments/production/models/example-model/promotions/example-promotion'})
            >>> # Creating a promotion with the same id and replace_if_exists=True will replace the promotion
            >>> model.promotions.create(
            ...     id="example-promotion",
            ...     model_version=model_version.name,
            ...     reason="MANUAL",
            ...     base_improvement_metric_value=0.8,
            ...     improvement_metric_value=0.9,
            ...     improvement_metric="accuracy",
            ...     tags={"test": "tag2"},
            ...     replace_if_exists=True,
            ... )
            <Promotion object {'name': 'projects/continual-test-proj/environments/production/models/example-model/promotions/example-promotion',
            'create_time': '2023-03-22T02:47:27.097419Z', 'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgd43u25lsriq8gqsamg',
            'improvement_metric': 'accuracy', 'improvement_metric_value': 0.9, 'base_improvement_metric_value': 0.8,
            'improvement_metric_diff': 0.09999999999999998, 'reason': 'MANUAL', 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'tags': {'test': 'tag2'}, 'base_model_version': '', 'message': '', 'account': ''}>

        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")
        assert isinstance(improvement_metric_value, float) or isinstance(
            improvement_metric_value, int
        ), ValueError("Improvement metric value must be a float or int")
        assert isinstance(base_improvement_metric_value, float) or isinstance(
            base_improvement_metric_value, int
        ), ValueError("Base improvement metric value must be a float or int")

        req = management_pb2.CreatePromotionRequest(
            parent=self.parent,
            promotion=Promotion(
                reason=reason,
                base_model_version=base_model_version,
                model_version=self.name(
                    model_version,
                    self.parent,
                    f"{self.parent}/versions/{id}",
                ),
                improvement_metric=improvement_metric,
                improvement_metric_value=improvement_metric_value,
                base_improvement_metric_value=base_improvement_metric_value,
                improvement_metric_diff=(
                    improvement_metric_value - base_improvement_metric_value
                ),
                message=message,
                tags=tags,
                run=self.run_name,
                current_run=self.run_name,
            ).to_proto(),
            promotion_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreatePromotion(req)
        return Promotion.from_proto(resp, client=self.client, current_run=self.run_name)

    def get(self, id: str) -> Promotion:
        """Get promotion.

        Arguments:
            id: Promotion name or id.

        Returns
            A promotion.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> promotion = model.promotions.create(
            ...     id="example-promotion",
            ...     model_version=model_version.name,
            ...     reason="UPLIFT",
            ...     base_improvement_metric_value=0.8,
            ...     improvement_metric_value=0.9,
            ...     improvement_metric="accuracy",
            ...     tags={"test": "tag"},
            ... )
            >>> model.promotions.get("example-promotion")
            <Promotion object {'name': 'projects/continual-test-proj/environments/production/models/example-model/promotions/example-promotion',
            'create_time': '2023-03-22T02:47:27.097419Z', 'model_version': 'projects/continual-test-proj/environments/production/models/example-model/versions/cgd43u25lsriq8gqsamg',
            'improvement_metric': 'accuracy', 'improvement_metric_value': 0.9, 'base_improvement_metric_value': 0.8,
            'improvement_metric_diff': 0.09999999999999998, 'reason': 'UPLIFT', 'run': 'projects/continual-test-proj/environments/production/runs/cgcu3h25lsriq8gqs8og',
            'tags': {'test': 'tag'}, 'base_model_version': '', 'message': '', 'account': ''}>
        """
        req = management_pb2.GetPromotionRequest(name=self.name(id))
        resp = self.client._management.GetPromotion(req)
        return Promotion.from_proto(resp, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        default_sort_order: str = "ASC",
    ) -> List[Promotion]:
        """List promotions.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Promotions.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> promos = [
            ...     model.promotions.create(
            ...         id=f"promo-{i}",
            ...         model_version=model_version.name,
            ...         improvement_metric=f"accuracy-{5-i}",
            ...         improvement_metric_value=0.1*(i+1))
            ...     for i in range(5)
            ... ]
            >>> [p.id for p in model.promotions.list(page_size=10)]
            ['promo-0', 'promo-1', 'promo-2', 'promo-3', 'promo-4']
            >>> [p.id for p in model.promotions.list(page_size=10, order_by="improvement_metric")]
            ['promo-4', 'promo-3', 'promo-2', 'promo-1', 'promo-0']
            >>> [p.id for p in model.promotions.list(page_size=10, order_by="improvement_metric", default_sort_order="DESC")]
            ['promo-0', 'promo-1', 'promo-2', 'promo-3', 'promo-4']
        """
        req = management_pb2.ListPromotionsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListPromotions(req)
        return [
            Promotion.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.promotions
        ]

    def list_all(self) -> Pager[Promotion]:
        """List all promotions.

        Pages through all promotions using an iterator.

        Returns:
            A iterator of all promotions.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> promos = [
            ...     model.promotions.create(
            ...         id=f"promo-{i}",
            ...         model_version=model_version.name,
            ...         improvement_metric=f"accuracy-{5-i}",
            ...         improvement_metric_value=0.1*(i+1))
            ...     for i in range(5)
            ... ]
            >>> [p.id for p in model.promotions.list_all()]
            ['promo-0', 'promo-1', 'promo-2', 'promo-3', 'promo-4']
        """

        def next_page(next_page_token):
            req = management_pb2.ListPromotionsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListPromotions(req)
            return (
                [
                    Promotion.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.promotions
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        promotion: Promotion,
    ) -> Promotion:
        """Update Promotion.

        Arguments:
            paths: A list of paths to be updated.
            promotion: Promotion object containing updated fields.

        Returns:
            An updated Promotion.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> promotion = model.promotions.create(
            ...     id="example-promotion",
            ...     model_version=model_version.name,
            ...     reason="UPLIFT",
            ...     base_improvement_metric_value=0.8,
            ...     improvement_metric_value=0.9,
            ...     improvement_metric="accuracy",
            ...     tags={"test": "tag"},
            ... )
            >>> promotions.improvement_metric_value
            0.9
            >>> promotion.improvement_metric_value = 0.95
            >>> new_promotion = model.promotions.update(
            ...     paths=["improvement_metric_value"],
            ...     promotion=promotion,
            ... )
            >>> new_promotion.improvement_metric_value
            0.95
        """

        req = management_pb2.UpdatePromotionRequest(
            promotion=promotion.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdatePromotion(req)
        return Promotion.from_proto(resp, client=self.client, current_run=self.run_name)

    def _get_latest_promotion(self) -> Promotion:
        """Get latest promotion.

        Returns:
            The most recently created Promotion.

        Examples:
            >>> ...
        """
        req = management_pb2.GetLatestPromotionRequest(parent=self.parent)
        resp = self.client._management.GetLatestPromotion(req)
        return Promotion.from_proto(resp, client=self.client, current_run=self.run_name)


class Promotion(Resource, types.Promotion):
    """Promotion resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/promotions/{promotion}"
    _manager: PromotionManager
    """Promotion Manager."""

    _metadata: MetadataManager
    """Metadata Manager"""

    def _init(self):
        self._manager = PromotionManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._metadata = MetadataManager(
            parent=self.name, client=self.client, run_name=self.current_run
        )

    @property
    def metadata(self) -> MetadataManager:
        """Metadata Manager"""
        return self._metadata

    def update(self, paths: List[str]) -> Promotion:
        """Update Promotion.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Promotion.

        Examples:
            >>> # model is a Model object and model_version is a ModelVersion object
            >>> promotion = model.promotions.create(
            ...     id="example-promotion",
            ...     model_version=model_version.name,
            ...     reason="UPLIFT",
            ...     base_improvement_metric_value=0.8,
            ...     improvement_metric_value=0.9,
            ...     improvement_metric="accuracy",
            ...     tags={"test": "tag"},
            ... )
            >>> promotions.improvement_metric_value
            0.9
            >>> promotion.improvement_metric_value = 0.95
            >>> new_promotion = promotion.update(paths=["improvement_metric_value"])
            >>> new_promotion.improvement_metric_value
            0.95
        """
        return self._manager.update(paths=paths, promotion=self)

    def add_tags(self, tags: dict[str, str]) -> Promotion:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Promotion.

        Examples:
            >>> # promotion is a Promotion object with tags {"color": "red"}
            >>> promotion.tags
            {'color': 'red'}
            >>> updated_promotion = promotion.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_promotion.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(promotion=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Promotion:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Promotion.

        Examples:
            >>> # promotion is a Promotion object with tags {"color": "red"}
            >>> promotion.tags
            {'color': 'red'}
            >>> updated_promotion = promotion.remove_tags(["color", "fruit"])
            >>> updated_promotion.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(promotion=self, paths=["tags"])
