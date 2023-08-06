import terrascript.core as core


@core.resource(type="aws_ram_resource_association", namespace="aws_ram")
class ResourceAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    resource_arn: str | core.StringOut = core.attr(str)

    resource_share_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_arn: str | core.StringOut,
        resource_share_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceAssociation.Args(
                resource_arn=resource_arn,
                resource_share_arn=resource_share_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_arn: str | core.StringOut = core.arg()

        resource_share_arn: str | core.StringOut = core.arg()
