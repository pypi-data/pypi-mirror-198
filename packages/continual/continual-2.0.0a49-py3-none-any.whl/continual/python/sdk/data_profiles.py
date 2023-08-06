from __future__ import annotations
from typing import List, Optional
import pandas as pd
import copy

from continual.python.sdk.iterators import Pager

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager

from continual.python.sdk.utils import (
    _get_feature_analysis,
    _get_correlation_matrix,
    _get_dataset_ranges,
    _get_non_unique_index_count,
)


class DataProfilesManager(Manager):
    """Manages DataProfile resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/datasets/{dataset}/versions/{version}/dataProfiles/{data_profile}"

    def create(
        self,
        dataframes: List[pd.DataFrame],
        entry_names: List[str],
        index_column: str,
        datetime_columns: List[str] = [],
        time_index_column: str = None,
        id: Optional[str] = "",
        tags: Optional[dict[str, str]] = [],
        replace_if_exists: bool = False,
    ) -> DataProfile:
        """Create an data profile.

        Arguments:
            dataframes: List of dataframes on which to compute stats
            entry_names: A label for each dataset stats entry (corresponds to a dataframe)
            datetime_columns: List of columns that contain datetime values
            index_column: Name of the index column
            time_index_column: Name of the time index column
            id: DataProfile's name or id.
            tags: A dictionary of tags to associate with the data profile.
            replace_if_exists: If True, and the data profile exists it will be replaced with the new data_profile

        Returns:
            A DataProfile object.

        Examples:
            >>> ... # Assume client, project, environment, and dataset are defined
            >>> import pandas as pd
            >>> num_rows = 450
            >>> data = pd.DataFrame(
            ... {
            ...     "index_col": list(range(num_rows)),
            ...     "time_index_col": pd.date_range(
            ...                         datetime.date.today(), periods=num_rows
            ...                     ).tolist(),
            ...     "timestamp_col": pd.date_range(
            ...                         datetime.date.today(), periods=num_rows, freq="2D"
            ...                     ).tolist(),
            ...     "float_col": [i * 4.0 for i in range(num_rows)],
            ...     "int_col": list(range(num_rows)),
            ...     "str_col": [f"test_val_{i}" for i in range(num_rows)],
            ...     "bool_col": [i % 2 == 0 for i in range(num_rows)],
            ...     "categorical_types": [
            ...         np.random.choice(["CAT", "DOG", "COW", "RAT"]) for _ in range(num_rows)
            ...     ],
            ...   })
            >>> dataset_version = dataset.dataset_versions.create()
            >>> dataset_version.data_profiles.create(
            ...         dataframes=[data],
            ...         entry_names=["test_entry"],
            ...         datetime_columns=["time_index_col", "timestamp_col"],
            ...         index_column="index_col",
            ...         time_index_column="time_index_col",
            ...     )
            <DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegi8k25lsrt9r5a8ni0',
            'dataset_stats': [{'entry_name': 'test_entry', 'num_examples': '450',
            'correlation_matrix': {'display_names': ['index_col', 'float_col', 'int_col', 'bool_col'], 'rows':...
        """
        if tags:
            assert all(
                [isinstance(k, str) and isinstance(v, str) for k, v in tags.items()]
            ), ValueError("Tags must be a dict of str: str")

        dataset_stats = []
        for entry_name, data in zip(entry_names, dataframes):
            profile_datetime_cols = copy.deepcopy(datetime_columns)
            if time_index_column:
                profile_datetime_cols.append(time_index_column)

            results = {}
            results["entry_name"] = entry_name
            results["num_examples"] = data.shape[0]

            # only generate a correlation matri if there is more than 1 column
            if len(data.columns) > 1:
                results["correlation_matrix"] = _get_correlation_matrix(data)

            (
                results["numeric_stats"],
                results["string_stats"],
                results["categorical_stats"],
                results["timestamp_stats"],
            ) = _get_feature_analysis(data, datetime_columns, index_column=index_column)
            results["duplicate_rows"] = int(data.duplicated().sum())
            results["duplicate_indexes"] = _get_non_unique_index_count(
                data, index_col=index_column, time_index_col=time_index_column
            )

            results["dataset_ranges"] = _get_dataset_ranges(
                data=data,
                columns=profile_datetime_cols,
            )
            dataset_stats.append(results)

        req = management_pb2.CreateDataProfileRequest(
            parent=self.parent,
            data_profile=DataProfile(
                dataset_stats=dataset_stats,
                tags=tags,
                run=self.run_name,
                current_run=self.run_name,
            ).to_proto(),
            data_profile_id=id,
            replace_if_exists=replace_if_exists,
        )

        resp = self.client._management.CreateDataProfile(req)
        return DataProfile.from_proto(
            resp, client=self.client, current_run=self.run_name
        )

    def get(self, id: str) -> DataProfile:
        """Get data_profile.

        Arguments:
            id: DataProfile name or id.

        Returns
            A data_profile.

        Examples:
            >>> ... # Assume dataset and dataset version is defined and a data profile is created
            >>> profile = dataset_version.data_profiles.create(
            ...         dataframes=[data],
            ...         entry_names=["test_entry"],
            ...         datetime_columns=["time_index_col", "timestamp_col"],
            ...         index_column="index_col",
            ...         time_index_column="time_index_col",
            ...     )
            >>> dataset_version.data_profiles.get(profile.id)
            <DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegi8k25lsrt9r5a8ni0',
            'dataset_stats': [{'entry_name': 'test_entry', 'num_examples': '450',
            'correlation_matrix': {'display_names': ['index_col', 'float_col', 'int_col', 'bool_col'], 'rows':...
        """

        req = management_pb2.GetDataProfileRequest(name=self.name(id))
        data_profile = self.client._management.GetDataProfile(req)
        return DataProfile.from_proto(
            data_profile, client=self.client, current_run=self.run_name
        )

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        default_sort_order: str = "ASC",
    ) -> List[DataProfile]:
        """List data profiles.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            latest: If true, the results are sorted in descending order, else ascending.

        Returns:
            A list of DataProfiles.

        Examples:
            >>> ... # Assume dataset and dataset version is defined and a data profile is created
            >>> [dataset_version.data_profiles.create(
            ...         dataframes=[data],
            ...         entry_names=["test_entry"],
            ...         datetime_columns=["time_index_col", "timestamp_col"],
            ...         index_column="index_col",
            ...         time_index_column="time_index_col",
            ...     ) for _ in range(3)]
            >>> [p.name for p in dataset_version.data_profiles.list(page_size=3))]
            [<DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegiasd0123ksrt9va8ni0'...
            ,<DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegi8k25lkjkl3t9r5a4vi0'...
            ,<DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegi8k25lsrt9rasd5a8ni0'...]
        """
        req = management_pb2.ListDataProfilesRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            default_sort_order=default_sort_order,
        )
        resp = self.client._management.ListDataProfiles(req)
        return [
            DataProfile.from_proto(x, client=self.client, current_run=self.run_name)
            for x in resp.data_profiles
        ]

    def list_all(self, resource_name: str) -> Pager[DataProfile]:
        """List all data profiles.

        Pages through all data profiles using an iterator.

        Returns:
            A iterator of all DataProfiles.

        Examples:
            >>> ... # Assume dataset and dataset version is defined and a data profile is created
            >>> [dataset_version.data_profiles.create(
            ...         dataframes=[data],
            ...         entry_names=["test_entry"],
            ...         datetime_columns=["time_index_col", "timestamp_col"],
            ...         index_column="index_col",
            ...         time_index_column="time_index_col",
            ...     ) for _ in range(3)]
            >>> [p.name for p in dataset_version.data_profiles.list_all())]
            [<DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegiasd0123ksrt9va8ni0'...
            ,<DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegi8k25lkjkl3t9r5a4vi0'...
            ,<DataProfile object {'name': 'projects/continual_test_proj/environments/production/datasets/breast_cancer_dataset/versions/cegi8j25lsrt9r5a8ngg/data_profiles/cegi8k25lsrt9rasd5a8ni0'...]
        """

        def next_page(next_page_token):
            req = management_pb2.ListDataProfilesRequest(
                resource_name=resource_name, page_token=next_page_token
            )
            resp = self.client._management.ListDataProfiles(req)
            return (
                [
                    DataProfile.from_proto(
                        x, client=self.client, current_run=self.run_name
                    )
                    for x in resp.data_profiles
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def update(
        self,
        paths: List[str],
        data_profile: DataProfile,
    ) -> DataProfile:
        """Update DataProfile.

        Arguments:
            paths: A list of paths to be updated.
            data_profile: DataProfile object containing updated fields.

        Returns:
            An updated DataProfile.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
        """

        req = management_pb2.UpdateDataProfileRequest(
            data_profile=data_profile.to_proto(),
            update_paths=paths,
            run=self.run_name,
        )
        resp = self.client._management.UpdateDataProfile(req)
        return DataProfile.from_proto(
            resp, client=self.client, current_run=self.run_name
        )


class DataProfile(Resource, types.DataProfile):
    """DataProfile resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/datasets/{dataset}/versions/{version}/dataProfiles/{dataProfile}"

    _manager: DataProfilesManager
    """DataProfile Manager."""

    def _init(self):
        self._manager = DataProfilesManager(
            parent=self.parent, client=self.client, run_name=self.current_run
        )

    def update(self, paths: List[str]) -> DataProfile:
        """Update DataProfile.

        Arguments:
            paths: A list of paths to be updated.

        Returns:
            An updated DataProfile.

        Examples:
            >>> ...
        """
        return self._manager.update(paths=paths, data_profile=self)

    def add_tags(self, tags: dict[str, str]) -> DataProfile:
        """add tags.

        Arguments:
            tags: A dictionary of tag key/tag value

        Returns:
            An updated DataProfile.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> data_profile = dataset_version.data_profiles.get("test-data-profile")
            >>> data_profile.add_tags({"color": "blue", "fruit": "apple"})
        """
        for key in tags:
            self.tags[key] = tags[key]
        return self._manager.update(data_profile=self, paths=["tags"])

    def remove_tags(self, tags: List[str]) -> DataProfile:
        """remove tags.

        Arguments:
            tags: A list of tag keys

        Returns:
            An updated DataProfile.

        Examples:
            >>> ... # Assuming client, org and project is already authenticated
            >>> data_profile = dataset_version.data_profiles.get("test-data-profile")
            >>> data_profile.remove_tags({"color", "fruit"})
        """
        for key in tags:
            self.tags.pop(key, -1)
        return self._manager.update(data_profile=self, paths=["tags"])
