"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import ...muses.v1.flow_service_pb2

class FlowServiceStub:
    """The service that handles the CRUD of Flow."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateFlow: grpc.UnaryUnaryMultiCallable[
        muses.v1.flow_service_pb2.CreateFlowRequest,
        muses.v1.flow_service_pb2.CreateFlowResponse]
    """Creates a Flow."""

    GetFlow: grpc.UnaryUnaryMultiCallable[
        muses.v1.flow_service_pb2.GetFlowRequest,
        muses.v1.flow_service_pb2.GetFlowResponse]
    """Gets a Flow."""

    UpdateFlow: grpc.UnaryUnaryMultiCallable[
        muses.v1.flow_service_pb2.UpdateFlowRequest,
        muses.v1.flow_service_pb2.UpdateFlowResponse]
    """Updates a Flow."""

    ListFlows: grpc.UnaryUnaryMultiCallable[
        muses.v1.flow_service_pb2.ListFlowsRequest,
        muses.v1.flow_service_pb2.ListFlowsResponse]
    """Lists Flows in a Location."""

    DeleteFlow: grpc.UnaryUnaryMultiCallable[
        muses.v1.flow_service_pb2.DeleteFlowRequest,
        muses.v1.flow_service_pb2.DeleteFlowResponse]
    """Deletes a Flow."""

    DeleteFlows: grpc.UnaryUnaryMultiCallable[
        muses.v1.flow_service_pb2.DeleteFlowsRequest,
        muses.v1.flow_service_pb2.DeleteFlowsResponse]
    """Batch delete Flow by filter."""


class FlowServiceServicer(metaclass=abc.ABCMeta):
    """The service that handles the CRUD of Flow."""
    @abc.abstractmethod
    def CreateFlow(self,
        request: muses.v1.flow_service_pb2.CreateFlowRequest,
        context: grpc.ServicerContext,
    ) -> muses.v1.flow_service_pb2.CreateFlowResponse:
        """Creates a Flow."""
        pass

    @abc.abstractmethod
    def GetFlow(self,
        request: muses.v1.flow_service_pb2.GetFlowRequest,
        context: grpc.ServicerContext,
    ) -> muses.v1.flow_service_pb2.GetFlowResponse:
        """Gets a Flow."""
        pass

    @abc.abstractmethod
    def UpdateFlow(self,
        request: muses.v1.flow_service_pb2.UpdateFlowRequest,
        context: grpc.ServicerContext,
    ) -> muses.v1.flow_service_pb2.UpdateFlowResponse:
        """Updates a Flow."""
        pass

    @abc.abstractmethod
    def ListFlows(self,
        request: muses.v1.flow_service_pb2.ListFlowsRequest,
        context: grpc.ServicerContext,
    ) -> muses.v1.flow_service_pb2.ListFlowsResponse:
        """Lists Flows in a Location."""
        pass

    @abc.abstractmethod
    def DeleteFlow(self,
        request: muses.v1.flow_service_pb2.DeleteFlowRequest,
        context: grpc.ServicerContext,
    ) -> muses.v1.flow_service_pb2.DeleteFlowResponse:
        """Deletes a Flow."""
        pass

    @abc.abstractmethod
    def DeleteFlows(self,
        request: muses.v1.flow_service_pb2.DeleteFlowsRequest,
        context: grpc.ServicerContext,
    ) -> muses.v1.flow_service_pb2.DeleteFlowsResponse:
        """Batch delete Flow by filter."""
        pass


def add_FlowServiceServicer_to_server(servicer: FlowServiceServicer, server: grpc.Server) -> None: ...
