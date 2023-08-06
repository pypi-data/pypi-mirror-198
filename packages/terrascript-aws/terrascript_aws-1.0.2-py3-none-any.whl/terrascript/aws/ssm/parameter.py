import terrascript.core as core


@core.resource(type="aws_ssm_parameter", namespace="aws_ssm")
class Parameter(core.Resource):

    allowed_pattern: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    data_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    insecure_value: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    overwrite: bool | core.BoolOut | None = core.attr(bool, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        allowed_pattern: str | core.StringOut | None = None,
        arn: str | core.StringOut | None = None,
        data_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        insecure_value: str | core.StringOut | None = None,
        key_id: str | core.StringOut | None = None,
        overwrite: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tier: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Parameter.Args(
                name=name,
                type=type,
                allowed_pattern=allowed_pattern,
                arn=arn,
                data_type=data_type,
                description=description,
                insecure_value=insecure_value,
                key_id=key_id,
                overwrite=overwrite,
                tags=tags,
                tags_all=tags_all,
                tier=tier,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_pattern: str | core.StringOut | None = core.arg(default=None)

        arn: str | core.StringOut | None = core.arg(default=None)

        data_type: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        insecure_value: str | core.StringOut | None = core.arg(default=None)

        key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        overwrite: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tier: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut | None = core.arg(default=None)
