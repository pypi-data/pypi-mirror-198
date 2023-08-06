import terrascript.core as core


@core.resource(type="aws_lakeformation_resource", namespace="lakeformation")
class Resource(core.Resource):

    arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The date and time the resource was last modified in [RFC 3339 format](https://tools.ietf.
    org/html/rfc3339#section-5.8).
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        arn: str | core.StringOut,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resource.Args(
                arn=arn,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)
