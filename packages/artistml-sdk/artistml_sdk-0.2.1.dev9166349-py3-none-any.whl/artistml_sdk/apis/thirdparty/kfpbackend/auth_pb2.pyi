"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AuthorizeRequest(google.protobuf.message.Message):
    """Ask for authorization of an access by providing resource's namespace, type
    and verb. User identity is not part of the message, because it is expected
    to be parsed from request headers. Caller should proxy user request's headers.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Resources:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ResourcesEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AuthorizeRequest._Resources.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNASSIGNED_RESOURCES: AuthorizeRequest._Resources.ValueType  # 0
        VIEWERS: AuthorizeRequest._Resources.ValueType  # 1
    class Resources(_Resources, metaclass=_ResourcesEnumTypeWrapper):
        """Type of resources in pipelines system."""
        pass

    UNASSIGNED_RESOURCES: AuthorizeRequest.Resources.ValueType  # 0
    VIEWERS: AuthorizeRequest.Resources.ValueType  # 1

    class _Verb:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _VerbEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AuthorizeRequest._Verb.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNASSIGNED_VERB: AuthorizeRequest._Verb.ValueType  # 0
        CREATE: AuthorizeRequest._Verb.ValueType  # 1
        GET: AuthorizeRequest._Verb.ValueType  # 2
        DELETE: AuthorizeRequest._Verb.ValueType  # 3
    class Verb(_Verb, metaclass=_VerbEnumTypeWrapper):
        """Type of verbs that act on the resources."""
        pass

    UNASSIGNED_VERB: AuthorizeRequest.Verb.ValueType  # 0
    CREATE: AuthorizeRequest.Verb.ValueType  # 1
    GET: AuthorizeRequest.Verb.ValueType  # 2
    DELETE: AuthorizeRequest.Verb.ValueType  # 3

    NAMESPACE_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    VERB_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    """Namespace the resource belongs to."""

    resources: global___AuthorizeRequest.Resources.ValueType
    """Resource type asking for authorization."""

    verb: global___AuthorizeRequest.Verb.ValueType
    """Verb on the resource asking for authorization."""

    def __init__(self,
        *,
        namespace: typing.Text = ...,
        resources: global___AuthorizeRequest.Resources.ValueType = ...,
        verb: global___AuthorizeRequest.Verb.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["namespace",b"namespace","resources",b"resources","verb",b"verb"]) -> None: ...
global___AuthorizeRequest = AuthorizeRequest
