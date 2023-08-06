from __future__ import annotations
from typing import List, Optional
from continual.python.sdk.iterators import Pager

from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.events import EventManager
from continual.rpc.management.v1 import management_pb2, types

CHUNK_SIZE = 117440512  # 112 MB in bytes, chosen arbitrarily


class ChecksManager(Manager):
    """Manages checks."""

    # the name pattern for a check depends on the resource it was created for
    name_pattern: str = ""

    def create(
        self,
        display_name: str,
        outcome: str,
        message: str = "",
        current_value: Optional[float] = 0.0,
        baseline_value: Optional[float] = 0.0,
        id: Optional[str] = None,
        replace_if_exists: bool = False,
    ) -> Check:
        """Create a Check.
        Arguments:
            display_name: Display name of the check.
            outcome: whether the check PASSED, FAILED, or was SKIPPED.
            message: A message describing the check.
            current_value: A numeric value that is the current value that is the basis for the check
            baseline_value: A numeric value that is being compared the current value.
            id: Optional ID of the check.
            replace_if_exists: If true, replace the check if it already exists.

        Returns:
            Check object.

        Examples:
            >>> # dataset_version is a DatasetVersion object
            >>> dataset_version.checks.create(
            ...         display_name="Improve model accuracy by at least 5%",
            ...         outcome="PASSED",
            ...         message="Improved model accuracy",
            ...         current_value=0.6,
            ...         baseline_value=0.45,
            ...     )
            <Check object {'name': 'projects/continual-test-proj/environments/production/datasets/test-dataset/versions/cgcecg25lsrvj7pl70jg/checks/cgcjg8a5lsrvj7pl71j0',
            'display_name': 'Improve model accuracy by at least 5%', 'run': 'projects/continual-test-proj/environments/production/runs/example-run',
            'message': 'Improved baseline accuracy by 5%', 'current_value': 0.5, 'baseline_value': 0.4, 'update_time': '2023-03-21T04:52:49.662518Z',
            'create_time': '2023-03-21T04:52:49.662518Z', 'outcome': 'PASSED'}>
        """
        req = management_pb2.CreateCheckRequest(
            parent=self.parent,
            check=Check(
                display_name=display_name,
                outcome=outcome,
                message=message,
                run=self.run_name,
                current_value=float(current_value)
                if isinstance(current_value, int)
                else current_value,
                baseline_value=float(baseline_value)
                if isinstance(baseline_value, int)
                else baseline_value,
                current_run=self.run_name,
            ).to_proto(),
            check_id=id,
            replace_if_exists=replace_if_exists,
        )
        resp = self.client._management.CreateCheck(req)
        return Check.from_proto(resp, client=self.client, current_run=self.run_name)

    def get(self, id: str) -> Check:
        """Get check.

        Arguments:
            id: Check name or id.

        Returns
            A Check.

        Examples:
            >>> # dataset_version is a DatasetVersion object
            >>> dataset_version.checks.create(
            ...         display_name="Improve model accuracy by at least 5%",
            ...         outcome="PASSED",
            ...         message="Improved model accuracy",
            ...         current_value=0.6,
            ...         baseline_value=0.45,
            ...     )
            >>> dataset_version.checks.get(id=dc.id)
            <Check object {'name': 'projects/continual-test-proj/environments/production/datasets/test-dataset/versions/cgcecg25lsrvj7pl70jg/checks/cgcjg8a5lsrvj7pl71j0',
            'display_name': 'Improve model accuracy by at least 5%', 'run': 'projects/continual-test-proj/environments/production/runs/example-run',
            'message': 'Improved baseline accuracy by 5%', 'current_value': 0.5, 'baseline_value': 0.4, 'update_time': '2023-03-21T04:52:49.662518Z',
            'create_time': '2023-03-21T04:52:49.662518Z', 'outcome': 'PASSED'}>
        """

        req = management_pb2.GetCheckRequest(
            name=self.name(
                id,
                parent=self.parent,
                name_pattern=f"{self.parent}/checks/{id}",
            )
        )
        check = self.client._management.GetCheck(req)
        return Check.from_proto(check, client=self.client, current_run=self.run_name)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[Check]:
        """List checks.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            default_sort_order: A string ('ASC' or 'DESC') default order by which to sort the list results.

        Returns:
            A list of Checks.

        Examples:
            >>> # dataset_version is a DatasetVersion object
            >>> checks = [
            ...     dataset_version.checks.create(
            ...             display_name=f"Test {i}",
            ...             outcome=f"{('PASSED' if i%2 == 1 else 'FAILED')}",
            ...             message=f"Test {i} {'passed' if i%2 == 1 else 'failed'}.")
            ...          for i in range(5)
            ... ]
            >>> [check.outcome for check in dataset_version.checks.list(page_size=10)]
            ['FAILED', 'PASSED', 'FAILED', 'PASSED', 'FAILED']
            >>> [check.outcome for check in dataset_version.checks.list(page_size=10, order_by='outcome')]
            ['FAILED', 'FAILED, 'FAILED', 'PASSED', 'PASSED']
            >>> [check.display_name for check in dataset_version.checks.list(page_size=10, order_by='display_name', default_sort_order='DESC')]
            ['Test 4', 'Test 3', 'Test 2', 'Test 1', 'Test 0']
        """
        req = management_pb2.ListChecksRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListChecks(req)
        return [
            Check.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.checks
        ]

    def list_all(self) -> Pager[Check]:
        """List all checks.
        Pages through all checks using an iterator.
        Returns:
            A iterator of all checks.
        Examples:
            >>> # dataset_version is a DatasetVersion object
            >>> checks = [dataset_version.checks.create(display_name=f"Test {i}", outcome='PASSED', message=f"Test {i} passed.") for i in range(5)]
            >>> [check.message for check in dataset_version.checks.list_all()]
            ['Test 0 passed.', 'Test 1 passed.', 'Test 2 passed.', 'Test 3 passed.', 'Test 4 passed.']
        """

        def next_page(next_page_token):
            req = management_pb2.ListChecksRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListChecks(req)
            return (
                [
                    Check.from_proto(x, client=self.client, current_run=self.run_name)
                    for x in resp.checks
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        check: Check,
    ) -> Check:
        """Update Check.

        Arguments:
            paths: A list of paths to be updated.
            check: Check object containing updated fields.

        Returns:
            An updated Check.

        Examples:
            >>> # dataset_version is a DatasetVersion object
            >>> check = dataset_version.checks.create(
            ...         display_name="Improve model accuracy by at least 5%",
            ...         outcome="PASSED",
            ...         message="Improved model accuracy",
            ...         current_value=0.6,
            ...         baseline_value=0.45,
            ...     )
            >>> check.message = "Improved baseline accuracy by 15%"
            >>> updated_check = dataset_version.checks.update(paths=["message"], check=check)
            >>> updated_check.message
            'Improved baseline accuracy by 15%'
        """

        req = management_pb2.UpdateCheckRequest(
            check=check.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateCheck(req)
        return Check.from_proto(resp, client=self.client, current_run=self.run_name)


class Check(Resource, types.Check):
    """Check check."""

    # the name pattern for check depends on the resource it was created for
    name_pattern: str = ""
    _manager: ChecksManager

    _events: EventManager
    """Event manager."""

    def _init(self):
        self._manager = ChecksManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )
        self._events = EventManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )

    @property
    def events(self) -> EventManager:
        """Get the Event manager.

        Returns:
            Event manager.
        """
        return self._events

    def update(self, paths: List[str]) -> Check:
        """Update Check.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated Check.

        Examples:
            >>> # dataset_version is a DatasetVersion object
            >>> check = dataset_version.checks.create(
            ...         display_name="Improve model accuracy by at least 5%",
            ...         outcome="PASSED",
            ...         message="Improved model accuracy",
            ...         current_value=0.6,
            ...         baseline_value=0.45,
            ...     )
            >>> check.message = "Improved baseline accuracy by 15%"
            >>> updated_check = check.update(paths=["message"])
            >>> updated_check.message
            'Improved baseline accuracy by 15%'
        """
        return self._manager.update(paths=paths, check=self)

    def add_tags(self, tags: dict[str, str]) -> Check:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated Check.

        Examples:
            >>> # check is a Check object with tags {"color": "red"}
            >>> check.tags
            {'color': 'red'}
            >>> updated_check = check.add_tags({"color": "blue", "fruit": "apple"})
            >>> updated_check.tags
            {'color': 'blue', 'fruit': 'apple'}
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(check=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> Check:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated Check.

        Examples:
            >>> # check is a Check object with tags {"color": "red"}
            >>> check.tags
            {'color': 'red'}
            >>> updated_check = check.remove_tags(["color", "fruit"])
            >>> updated_check.tags
            {}
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(check=self, paths=["tags"])
