import terrascript.core as core


@core.resource(type="aws_ec2_tag", namespace="aws_ec2")
class Tag(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str)

    resource_id: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key: str | core.StringOut,
        resource_id: str | core.StringOut,
        value: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Tag.Args(
                key=key,
                resource_id=resource_id,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()
