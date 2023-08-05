"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import ...thirdparty.kfpbackend.parameter_pb2
import ...thirdparty.kfpbackend.resource_reference_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Url(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIPELINE_URL_FIELD_NUMBER: builtins.int
    pipeline_url: typing.Text
    """URL of the pipeline definition or the pipeline version definition."""

    def __init__(self,
        *,
        pipeline_url: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pipeline_url",b"pipeline_url"]) -> None: ...
global___Url = Url

class CreatePipelineRequest(google.protobuf.message.Message):
    """Create pipeline by providing an URL pointing to the pipeline file,
    and optionally a pipeline name. If name is not provided, file name is used as
    pipeline name by default. Maximum size of 32MB is supported.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIPELINE_FIELD_NUMBER: builtins.int
    @property
    def pipeline(self) -> global___Pipeline: ...
    def __init__(self,
        *,
        pipeline: typing.Optional[global___Pipeline] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pipeline",b"pipeline"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pipeline",b"pipeline"]) -> None: ...
global___CreatePipelineRequest = CreatePipelineRequest

class UpdatePipelineDefaultVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIPELINE_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    pipeline_id: typing.Text
    """The ID of the pipeline to be updated."""

    version_id: typing.Text
    """The ID of the default version."""

    def __init__(self,
        *,
        pipeline_id: typing.Text = ...,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pipeline_id",b"pipeline_id","version_id",b"version_id"]) -> None: ...
global___UpdatePipelineDefaultVersionRequest = UpdatePipelineDefaultVersionRequest

class GetPipelineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """The ID of the pipeline to be retrieved."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___GetPipelineRequest = GetPipelineRequest

class ListPipelinesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    SORT_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    RESOURCE_REFERENCE_KEY_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    """A page token to request the next page of results. The token is acquried
    from the nextPageToken field of the response from the previous
    ListPipelines call.
    """

    page_size: builtins.int
    """The number of pipelines to be listed per page. If there are more pipelines
    than this number, the response message will contain a valid value in the
    nextPageToken field.
    """

    sort_by: typing.Text
    """Can be format of "field_name", "field_name asc" or "field_name desc"
    Ascending by default.
    """

    filter: typing.Text
    """A url-encoded, JSON-serialized Filter protocol buffer (see
    [filter.proto](https://github.com/kubeflow/pipelines/blob/master/backend/api/filter.proto)).
    """

    @property
    def resource_reference_key(self) -> thirdparty.kfpbackend.resource_reference_pb2.ResourceKey:
        """What resource reference to filter on.
        For Pipeline, the only valid resource type is Namespace. An sample query string could be
        resource_reference_key.type=NAMESPACE&resource_reference_key.id=ns1
        """
        pass
    def __init__(self,
        *,
        page_token: typing.Text = ...,
        page_size: builtins.int = ...,
        sort_by: typing.Text = ...,
        filter: typing.Text = ...,
        resource_reference_key: typing.Optional[thirdparty.kfpbackend.resource_reference_pb2.ResourceKey] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_reference_key",b"resource_reference_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","resource_reference_key",b"resource_reference_key","sort_by",b"sort_by"]) -> None: ...
global___ListPipelinesRequest = ListPipelinesRequest

class ListPipelinesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIPELINES_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def pipelines(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Pipeline]: ...
    total_size: builtins.int
    """The total number of pipelines for the given query."""

    next_page_token: typing.Text
    """The token to list the next page of pipelines."""

    def __init__(self,
        *,
        pipelines: typing.Optional[typing.Iterable[global___Pipeline]] = ...,
        total_size: builtins.int = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","pipelines",b"pipelines","total_size",b"total_size"]) -> None: ...
global___ListPipelinesResponse = ListPipelinesResponse

class GetPipelineByNameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    name: typing.Text
    """The Name of the pipeline to be retrieved."""

    namespace: typing.Text
    """The Namespace the pipeline belongs to.
    In the case of shared pipelines and KFPipeline standalone installation,
    the pipeline name is the only needed field for unique resource lookup (namespace is not required).
    In those case, please provide hyphen (dash character, "-").
    """

    def __init__(self,
        *,
        name: typing.Text = ...,
        namespace: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","namespace",b"namespace"]) -> None: ...
global___GetPipelineByNameRequest = GetPipelineByNameRequest

class DeletePipelineRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """The ID of the pipeline to be deleted."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___DeletePipelineRequest = DeletePipelineRequest

class GetTemplateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text
    """The ID of the pipeline whose template is to be retrieved."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id"]) -> None: ...
global___GetTemplateRequest = GetTemplateRequest

class GetTemplateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEMPLATE_FIELD_NUMBER: builtins.int
    template: typing.Text
    """The template of the pipeline specified in a GetTemplate request, or of a
    pipeline version specified in a GetPipelinesVersionTemplate request.
    """

    def __init__(self,
        *,
        template: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["template",b"template"]) -> None: ...
global___GetTemplateResponse = GetTemplateResponse

class GetPipelineVersionTemplateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSION_ID_FIELD_NUMBER: builtins.int
    version_id: typing.Text
    """The ID of the pipeline version whose template is to be retrieved."""

    def __init__(self,
        *,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["version_id",b"version_id"]) -> None: ...
global___GetPipelineVersionTemplateRequest = GetPipelineVersionTemplateRequest

class CreatePipelineVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def version(self) -> global___PipelineVersion:
        """ResourceReference inside PipelineVersion specifies the pipeline that this
        version belongs to.
        """
        pass
    def __init__(self,
        *,
        version: typing.Optional[global___PipelineVersion] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["version",b"version"]) -> None: ...
global___CreatePipelineVersionRequest = CreatePipelineVersionRequest

class GetPipelineVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSION_ID_FIELD_NUMBER: builtins.int
    version_id: typing.Text
    """The ID of the pipeline version to be retrieved."""

    def __init__(self,
        *,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["version_id",b"version_id"]) -> None: ...
global___GetPipelineVersionRequest = GetPipelineVersionRequest

class ListPipelineVersionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESOURCE_KEY_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    SORT_BY_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    @property
    def resource_key(self) -> thirdparty.kfpbackend.resource_reference_pb2.ResourceKey:
        """ResourceKey specifies the pipeline whose versions are to be listed."""
        pass
    page_size: builtins.int
    """The number of pipeline versions to be listed per page. If there are more
    pipeline versions than this number, the response message will contain a
    nextPageToken field you can use to fetch the next page.
    """

    page_token: typing.Text
    """A page token to request the next page of results. The token is acquried
    from the nextPageToken field of the response from the previous
    ListPipelineVersions call or can be omitted when fetching the first page.
    """

    sort_by: typing.Text
    """Can be format of "field_name", "field_name asc" or "field_name desc"
    Ascending by default.
    """

    filter: typing.Text
    """A base-64 encoded, JSON-serialized Filter protocol buffer (see
    filter.proto).
    """

    def __init__(self,
        *,
        resource_key: typing.Optional[thirdparty.kfpbackend.resource_reference_pb2.ResourceKey] = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
        sort_by: typing.Text = ...,
        filter: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resource_key",b"resource_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","resource_key",b"resource_key","sort_by",b"sort_by"]) -> None: ...
global___ListPipelineVersionsRequest = ListPipelineVersionsRequest

class ListPipelineVersionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    @property
    def versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PipelineVersion]: ...
    next_page_token: typing.Text
    """The token to list the next page of pipeline versions."""

    total_size: builtins.int
    """The total number of pipeline versions for the given query."""

    def __init__(self,
        *,
        versions: typing.Optional[typing.Iterable[global___PipelineVersion]] = ...,
        next_page_token: typing.Text = ...,
        total_size: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","total_size",b"total_size","versions",b"versions"]) -> None: ...
global___ListPipelineVersionsResponse = ListPipelineVersionsResponse

class DeletePipelineVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSION_ID_FIELD_NUMBER: builtins.int
    version_id: typing.Text
    """The ID of the pipeline version to be deleted."""

    def __init__(self,
        *,
        version_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["version_id",b"version_id"]) -> None: ...
global___DeletePipelineVersionRequest = DeletePipelineVersionRequest

class Pipeline(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    DEFAULT_VERSION_FIELD_NUMBER: builtins.int
    RESOURCE_REFERENCES_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Output. Unique pipeline ID. Generated by API server."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output. The time this pipeline is created."""
        pass
    name: typing.Text
    """Optional input field. Pipeline name provided by user. If not specified,
    file name is used as pipeline name.
    """

    description: typing.Text
    """Optional input field. Describing the purpose of the job."""

    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thirdparty.kfpbackend.parameter_pb2.Parameter]:
        """Output. The input parameters for this pipeline.
        TODO(jingzhang36): replace this parameters field with the parameters field
        inside PipelineVersion when all usage of the former has been changed to use
        the latter.
        """
        pass
    @property
    def url(self) -> global___Url:
        """The URL to the source of the pipeline. This is required when creating the
        pipeine through CreatePipeline API.
        TODO(jingzhang36): replace this url field with the code_source_urls field
        inside PipelineVersion when all usage of the former has been changed to use
        the latter.
        """
        pass
    error: typing.Text
    """In case any error happens retrieving a pipeline field, only pipeline ID
    and the error message is returned. Client has the flexibility of choosing
    how to handle error. This is especially useful during listing call.
    """

    @property
    def default_version(self) -> global___PipelineVersion:
        """Output only. The default version of the pipeline. As of now, the latest
        version is used as default. (In the future, if desired by customers, we
        can allow them to set default version.)
        """
        pass
    @property
    def resource_references(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thirdparty.kfpbackend.resource_reference_pb2.ResourceReference]:
        """Input field. Specify which resource this pipeline belongs to.
        For Pipeline, the only valid resource reference is a single Namespace.
        """
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name: typing.Text = ...,
        description: typing.Text = ...,
        parameters: typing.Optional[typing.Iterable[thirdparty.kfpbackend.parameter_pb2.Parameter]] = ...,
        url: typing.Optional[global___Url] = ...,
        error: typing.Text = ...,
        default_version: typing.Optional[global___PipelineVersion] = ...,
        resource_references: typing.Optional[typing.Iterable[thirdparty.kfpbackend.resource_reference_pb2.ResourceReference]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","default_version",b"default_version","url",b"url"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at",b"created_at","default_version",b"default_version","description",b"description","error",b"error","id",b"id","name",b"name","parameters",b"parameters","resource_references",b"resource_references","url",b"url"]) -> None: ...
global___Pipeline = Pipeline

class PipelineVersion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    CODE_SOURCE_URL_FIELD_NUMBER: builtins.int
    PACKAGE_URL_FIELD_NUMBER: builtins.int
    RESOURCE_REFERENCES_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Output. Unique version ID. Generated by API server."""

    name: typing.Text
    """Optional input field. Version name provided by user."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output. The time this pipeline version is created."""
        pass
    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thirdparty.kfpbackend.parameter_pb2.Parameter]:
        """Output. The input parameters for this pipeline."""
        pass
    code_source_url: typing.Text
    """Input. Optional. Pipeline version code source."""

    @property
    def package_url(self) -> global___Url:
        """Input. Required. Pipeline version package url.
        Whe calling CreatePipelineVersion API method, need to provide one package
        file location.
        """
        pass
    @property
    def resource_references(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[thirdparty.kfpbackend.resource_reference_pb2.ResourceReference]:
        """Input field. Specify which resource this pipeline version belongs to.
        For Experiment, the only valid resource reference is a single Namespace.
        """
        pass
    description: typing.Text
    """Input. Optional. Description for the pipeline version."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        name: typing.Text = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        parameters: typing.Optional[typing.Iterable[thirdparty.kfpbackend.parameter_pb2.Parameter]] = ...,
        code_source_url: typing.Text = ...,
        package_url: typing.Optional[global___Url] = ...,
        resource_references: typing.Optional[typing.Iterable[thirdparty.kfpbackend.resource_reference_pb2.ResourceReference]] = ...,
        description: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at",b"created_at","package_url",b"package_url"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["code_source_url",b"code_source_url","created_at",b"created_at","description",b"description","id",b"id","name",b"name","package_url",b"package_url","parameters",b"parameters","resource_references",b"resource_references"]) -> None: ...
global___PipelineVersion = PipelineVersion
