import terrascript.core as core


@core.resource(type="aws_wafv2_web_acl_association", namespace="waf")
class V2WebAclAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the resource to associate with the web ACL. This must b
    e an ARN of an Application Load Balancer or an Amazon API Gateway stage.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the Web ACL that you want to associate with the resourc
    e.
    """
    web_acl_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_arn: str | core.StringOut,
        web_acl_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2WebAclAssociation.Args(
                resource_arn=resource_arn,
                web_acl_arn=web_acl_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_arn: str | core.StringOut = core.arg()

        web_acl_arn: str | core.StringOut = core.arg()
