"""client for ArtistmlServer"""
from __future__ import annotations

from typing import final

import argo_workflows
from argo_workflows.api import workflow_service_api


@final
class ArgoClient:
    _configuration: argo_workflows.Configuration

    def __init__(self):
        super().__init__()

    def set_endpoint(self, endpoint: str, *args, **kwargs) -> ArgoClient:
        self._configuration = argo_workflows.Configuration(
            host=f"http://{endpoint}")
        self._configuration.verify_ssl = False
        return self

    @property
    def workflow(self) -> workflow_service_api.WorkflowServiceApi:
        api_client = argo_workflows.ApiClient(self._configuration)
        return workflow_service_api.WorkflowServiceApi(api_client)
