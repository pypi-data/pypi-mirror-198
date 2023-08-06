import terrascript.core as core


@core.schema
class Field(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    ref_value: str | core.StringOut = core.attr(str, computed=True)

    string_value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        ref_value: str | core.StringOut,
        string_value: str | core.StringOut,
    ):
        super().__init__(
            args=Field.Args(
                key=key,
                ref_value=ref_value,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        ref_value: str | core.StringOut = core.arg()

        string_value: str | core.StringOut = core.arg()


@core.schema
class PipelineObject(core.Schema):

    field: list[Field] | core.ArrayOut[Field] | None = core.attr(
        Field, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        name: str | core.StringOut,
        field: list[Field] | core.ArrayOut[Field] | None = None,
    ):
        super().__init__(
            args=PipelineObject.Args(
                id=id,
                name=name,
                field=field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field: list[Field] | core.ArrayOut[Field] | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Attribute(core.Schema):

    key: str | core.StringOut = core.attr(str, computed=True)

    string_value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        string_value: str | core.StringOut,
    ):
        super().__init__(
            args=Attribute.Args(
                key=key,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        string_value: str | core.StringOut = core.arg()


@core.schema
class ParameterObject(core.Schema):

    attribute: list[Attribute] | core.ArrayOut[Attribute] = core.attr(
        Attribute, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attribute: list[Attribute] | core.ArrayOut[Attribute],
        id: str | core.StringOut,
    ):
        super().__init__(
            args=ParameterObject.Args(
                attribute=attribute,
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute: list[Attribute] | core.ArrayOut[Attribute] = core.arg()

        id: str | core.StringOut = core.arg()


@core.schema
class ParameterValue(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    string_value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        string_value: str | core.StringOut,
    ):
        super().__init__(
            args=ParameterValue.Args(
                id=id,
                string_value=string_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        string_value: str | core.StringOut = core.arg()


@core.data(type="aws_datapipeline_pipeline_definition", namespace="datapipeline")
class DsPipelineDefinition(core.Data):
    """
    ID of the parameter object.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Parameter objects used in the pipeline definition. See below
    """
    parameter_object: list[ParameterObject] | core.ArrayOut[ParameterObject] = core.attr(
        ParameterObject, computed=True, kind=core.Kind.array
    )

    """
    Parameter values used in the pipeline definition. See below
    """
    parameter_value: list[ParameterValue] | core.ArrayOut[ParameterValue] | None = core.attr(
        ParameterValue, default=None, kind=core.Kind.array
    )

    """
    (Required) ID of the pipeline.
    """
    pipeline_id: str | core.StringOut = core.attr(str)

    """
    Objects defined in the pipeline. See below
    """
    pipeline_object: list[PipelineObject] | core.ArrayOut[PipelineObject] = core.attr(
        PipelineObject, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        pipeline_id: str | core.StringOut,
        parameter_value: list[ParameterValue] | core.ArrayOut[ParameterValue] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPipelineDefinition.Args(
                pipeline_id=pipeline_id,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_value: list[ParameterValue] | core.ArrayOut[ParameterValue] | None = core.arg(
            default=None
        )

        pipeline_id: str | core.StringOut = core.arg()
