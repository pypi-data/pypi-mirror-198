# Public SDK interface.
from continual.python.sdk.client import Client
from continual.python.sdk import exceptions
from continual.python.sdk.users import User
from continual.python.sdk.organizations import Organization
from continual.python.sdk.projects import Project
from continual.python.sdk.models import Model
from continual.python.sdk.model_versions import ModelVersion
from continual.python.sdk.experiments import Experiment
from continual.python.sdk.environments import Environment
from continual.python.sdk.promotions import Promotion
from continual.python.sdk.runs import Run
from continual.python.sdk.metrics import Metric
from continual.python.sdk.metadata import Metadata
from continual.python.sdk.data_profiles import DataProfile
from continual.python.sdk.checks import Check
from continual.python.sdk.datasets import Dataset
from continual.python.sdk.dataset_versions import DatasetVersion
from continual.python.sdk.dataset_version_assignments import DatasetVersionAssignment
from continual.python.sdk.artifacts import Artifact
from continual.python.sdk.endpoints import Endpoint

continual = Client(verify=False)
"""Client singleton.

To instantiate a custom client use `continual.Client()`.
"""


def version():
    return Client(verify=False).version()


__all__ = [
    "continual",
    "Client",
    "exceptions",
    "User",
    "Organization",
    "Project",
    "Connection",
    "Model",
    "ModelVersion",
    "Environment",
    "Experiment",
    "Promotion",
    "Run",
    "DataProfile",
    "Check",
    "Artifact",
    "Dataset",
    "DatasetVersion",
    "DatasetVersionAssignment",
    "Tag",
    "Metric",
    "Metadata",
    "Endpoint",
]
