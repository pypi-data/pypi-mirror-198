from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow import IoArgoprojWorkflowV1alpha1Workflow
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_create_request import (
    IoArgoprojWorkflowV1alpha1WorkflowCreateRequest, )

from ..gateway import argo_client


class ArgoClient:

    @staticmethod
    def tag():
        return "hello!"

    @property
    def _stub(self):
        """
        The function returns the vela client object
        :return: The vela client object
        """
        return argo_client

    # @try_request_grpc
    def create_workflow(
        self,
        namespace: str,
        body: IoArgoprojWorkflowV1alpha1WorkflowCreateRequest,
    ) -> IoArgoprojWorkflowV1alpha1Workflow:
        return self._stub.workflow.create_workflow(
            namespace=namespace,
            body=body,
            _check_return_type=False,
        )

    def get_workflow(
        self,
        namespace,
        name,
        **kwargs,
    ):
        return self._stub.workflow.get_workflow(
            namespace,
            name,
            **kwargs,
        )
