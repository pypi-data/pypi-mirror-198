import terrascript.core as core


@core.resource(type="aws_wafregional_web_acl_association", namespace="aws_wafregional")
class WebAclAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    resource_arn: str | core.StringOut = core.attr(str)

    web_acl_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_arn: str | core.StringOut,
        web_acl_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=WebAclAssociation.Args(
                resource_arn=resource_arn,
                web_acl_id=web_acl_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_arn: str | core.StringOut = core.arg()

        web_acl_id: str | core.StringOut = core.arg()
