import terrascript.core as core


@core.schema
class Attribute(core.Schema):

    key: str | core.StringOut = core.attr(str)

    string_value: str | core.StringOut = core.attr(str)

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

    attribute: list[Attribute] | core.ArrayOut[Attribute] | None = core.attr(
        Attribute, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        attribute: list[Attribute] | core.ArrayOut[Attribute] | None = None,
    ):
        super().__init__(
            args=ParameterObject.Args(
                id=id,
                attribute=attribute,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute: list[Attribute] | core.ArrayOut[Attribute] | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()


@core.schema
class ParameterValue(core.Schema):

    id: str | core.StringOut = core.attr(str)

    string_value: str | core.StringOut = core.attr(str)

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


@core.schema
class Field(core.Schema):

    key: str | core.StringOut = core.attr(str)

    ref_value: str | core.StringOut | None = core.attr(str, default=None)

    string_value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        ref_value: str | core.StringOut | None = None,
        string_value: str | core.StringOut | None = None,
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

        ref_value: str | core.StringOut | None = core.arg(default=None)

        string_value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class PipelineObject(core.Schema):

    field: list[Field] | core.ArrayOut[Field] | None = core.attr(
        Field, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

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


@core.resource(type="aws_datapipeline_pipeline_definition", namespace="datapipeline")
class PipelineDefinition(core.Resource):
    """
    (Required) ID of the object.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for the parameter objects used in the pipeline definition. See below
    """
    parameter_object: list[ParameterObject] | core.ArrayOut[ParameterObject] | None = core.attr(
        ParameterObject, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for the parameter values used in the pipeline definition. See below
    """
    parameter_value: list[ParameterValue] | core.ArrayOut[ParameterValue] | None = core.attr(
        ParameterValue, default=None, kind=core.Kind.array
    )

    """
    (Required) ID of the pipeline.
    """
    pipeline_id: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block for the objects that define the pipeline. See below
    """
    pipeline_object: list[PipelineObject] | core.ArrayOut[PipelineObject] = core.attr(
        PipelineObject, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        pipeline_id: str | core.StringOut,
        pipeline_object: list[PipelineObject] | core.ArrayOut[PipelineObject],
        parameter_object: list[ParameterObject] | core.ArrayOut[ParameterObject] | None = None,
        parameter_value: list[ParameterValue] | core.ArrayOut[ParameterValue] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PipelineDefinition.Args(
                pipeline_id=pipeline_id,
                pipeline_object=pipeline_object,
                parameter_object=parameter_object,
                parameter_value=parameter_value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        parameter_object: list[ParameterObject] | core.ArrayOut[ParameterObject] | None = core.arg(
            default=None
        )

        parameter_value: list[ParameterValue] | core.ArrayOut[ParameterValue] | None = core.arg(
            default=None
        )

        pipeline_id: str | core.StringOut = core.arg()

        pipeline_object: list[PipelineObject] | core.ArrayOut[PipelineObject] = core.arg()
