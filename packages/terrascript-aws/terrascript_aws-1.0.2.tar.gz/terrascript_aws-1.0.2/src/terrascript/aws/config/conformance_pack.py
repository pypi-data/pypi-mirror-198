import terrascript.core as core


@core.schema
class InputParameter(core.Schema):

    parameter_name: str | core.StringOut = core.attr(str)

    parameter_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        parameter_name: str | core.StringOut,
        parameter_value: str | core.StringOut,
    ):
        super().__init__(
            args=InputParameter.Args(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_name: str | core.StringOut = core.arg()

        parameter_value: str | core.StringOut = core.arg()


@core.resource(type="aws_config_conformance_pack", namespace="aws_config")
class ConformancePack(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    delivery_s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    delivery_s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.attr(
        InputParameter, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    template_body: str | core.StringOut | None = core.attr(str, default=None)

    template_s3_uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        delivery_s3_bucket: str | core.StringOut | None = None,
        delivery_s3_key_prefix: str | core.StringOut | None = None,
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = None,
        template_body: str | core.StringOut | None = None,
        template_s3_uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConformancePack.Args(
                name=name,
                delivery_s3_bucket=delivery_s3_bucket,
                delivery_s3_key_prefix=delivery_s3_key_prefix,
                input_parameter=input_parameter,
                template_body=template_body,
                template_s3_uri=template_s3_uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delivery_s3_bucket: str | core.StringOut | None = core.arg(default=None)

        delivery_s3_key_prefix: str | core.StringOut | None = core.arg(default=None)

        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        template_body: str | core.StringOut | None = core.arg(default=None)

        template_s3_uri: str | core.StringOut | None = core.arg(default=None)
