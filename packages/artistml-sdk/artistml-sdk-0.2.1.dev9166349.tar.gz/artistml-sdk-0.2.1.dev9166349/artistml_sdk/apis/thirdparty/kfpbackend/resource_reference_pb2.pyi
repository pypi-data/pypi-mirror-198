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

class _ResourceType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ResourceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResourceType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_RESOURCE_TYPE: _ResourceType.ValueType  # 0
    EXPERIMENT: _ResourceType.ValueType  # 1
    JOB: _ResourceType.ValueType  # 2
    PIPELINE: _ResourceType.ValueType  # 3
    PIPELINE_VERSION: _ResourceType.ValueType  # 4
    NAMESPACE: _ResourceType.ValueType  # 5
class ResourceType(_ResourceType, metaclass=_ResourceTypeEnumTypeWrapper):
    pass

UNKNOWN_RESOURCE_TYPE: ResourceType.ValueType  # 0
EXPERIMENT: ResourceType.ValueType  # 1
JOB: ResourceType.ValueType  # 2
PIPELINE: ResourceType.ValueType  # 3
PIPELINE_VERSION: ResourceType.ValueType  # 4
NAMESPACE: ResourceType.ValueType  # 5
global___ResourceType = ResourceType


class _Relationship:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _RelationshipEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Relationship.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_RELATIONSHIP: _Relationship.ValueType  # 0
    OWNER: _Relationship.ValueType  # 1
    CREATOR: _Relationship.ValueType  # 2
class Relationship(_Relationship, metaclass=_RelationshipEnumTypeWrapper):
    pass

UNKNOWN_RELATIONSHIP: Relationship.ValueType  # 0
OWNER: Relationship.ValueType  # 1
CREATOR: Relationship.ValueType  # 2
global___Relationship = Relationship


class ResourceKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    type: global___ResourceType.ValueType
    """The type of the resource that referred to."""

    id: typing.Text
    """The ID of the resource that referred to."""

    def __init__(self,
        *,
        type: global___ResourceType.ValueType = ...,
        id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","type",b"type"]) -> None: ...
global___ResourceKey = ResourceKey

class ResourceReference(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    RELATIONSHIP_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___ResourceKey: ...
    name: typing.Text
    """The name of the resource that referred to."""

    relationship: global___Relationship.ValueType
    """Required field. The relationship from referred resource to the object."""

    def __init__(self,
        *,
        key: typing.Optional[global___ResourceKey] = ...,
        name: typing.Text = ...,
        relationship: global___Relationship.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["key",b"key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","name",b"name","relationship",b"relationship"]) -> None: ...
global___ResourceReference = ResourceReference
