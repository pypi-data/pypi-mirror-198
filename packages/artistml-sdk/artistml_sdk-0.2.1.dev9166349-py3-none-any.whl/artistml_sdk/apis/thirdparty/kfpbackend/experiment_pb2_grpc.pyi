"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.empty_pb2
import grpc
import ...thirdparty.kfpbackend.experiment_pb2

class ExperimentServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateExperiment: grpc.UnaryUnaryMultiCallable[
        thirdparty.kfpbackend.experiment_pb2.CreateExperimentRequest,
        thirdparty.kfpbackend.experiment_pb2.Experiment]
    """Creates a new experiment."""

    GetExperiment: grpc.UnaryUnaryMultiCallable[
        thirdparty.kfpbackend.experiment_pb2.GetExperimentRequest,
        thirdparty.kfpbackend.experiment_pb2.Experiment]
    """Finds a specific experiment by ID."""

    ListExperiment: grpc.UnaryUnaryMultiCallable[
        thirdparty.kfpbackend.experiment_pb2.ListExperimentsRequest,
        thirdparty.kfpbackend.experiment_pb2.ListExperimentsResponse]
    """Finds all experiments. Supports pagination, and sorting on certain fields."""

    DeleteExperiment: grpc.UnaryUnaryMultiCallable[
        thirdparty.kfpbackend.experiment_pb2.DeleteExperimentRequest,
        google.protobuf.empty_pb2.Empty]
    """Deletes an experiment without deleting the experiment's runs and jobs. To
    avoid unexpected behaviors, delete an experiment's runs and jobs before
    deleting the experiment.
    """

    ArchiveExperiment: grpc.UnaryUnaryMultiCallable[
        thirdparty.kfpbackend.experiment_pb2.ArchiveExperimentRequest,
        google.protobuf.empty_pb2.Empty]
    """Archives an experiment and the experiment's runs and jobs."""

    UnarchiveExperiment: grpc.UnaryUnaryMultiCallable[
        thirdparty.kfpbackend.experiment_pb2.UnarchiveExperimentRequest,
        google.protobuf.empty_pb2.Empty]
    """Restores an archived experiment. The experiment's archived runs and jobs
    will stay archived.
    """


class ExperimentServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateExperiment(self,
        request: thirdparty.kfpbackend.experiment_pb2.CreateExperimentRequest,
        context: grpc.ServicerContext,
    ) -> thirdparty.kfpbackend.experiment_pb2.Experiment:
        """Creates a new experiment."""
        pass

    @abc.abstractmethod
    def GetExperiment(self,
        request: thirdparty.kfpbackend.experiment_pb2.GetExperimentRequest,
        context: grpc.ServicerContext,
    ) -> thirdparty.kfpbackend.experiment_pb2.Experiment:
        """Finds a specific experiment by ID."""
        pass

    @abc.abstractmethod
    def ListExperiment(self,
        request: thirdparty.kfpbackend.experiment_pb2.ListExperimentsRequest,
        context: grpc.ServicerContext,
    ) -> thirdparty.kfpbackend.experiment_pb2.ListExperimentsResponse:
        """Finds all experiments. Supports pagination, and sorting on certain fields."""
        pass

    @abc.abstractmethod
    def DeleteExperiment(self,
        request: thirdparty.kfpbackend.experiment_pb2.DeleteExperimentRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """Deletes an experiment without deleting the experiment's runs and jobs. To
        avoid unexpected behaviors, delete an experiment's runs and jobs before
        deleting the experiment.
        """
        pass

    @abc.abstractmethod
    def ArchiveExperiment(self,
        request: thirdparty.kfpbackend.experiment_pb2.ArchiveExperimentRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """Archives an experiment and the experiment's runs and jobs."""
        pass

    @abc.abstractmethod
    def UnarchiveExperiment(self,
        request: thirdparty.kfpbackend.experiment_pb2.UnarchiveExperimentRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty:
        """Restores an archived experiment. The experiment's archived runs and jobs
        will stay archived.
        """
        pass


def add_ExperimentServiceServicer_to_server(servicer: ExperimentServiceServicer, server: grpc.Server) -> None: ...
