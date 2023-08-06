import terrascript.core as core


@core.data(type="aws_wafv2_web_acl", namespace="waf")
class DsV2WebAcl(core.Data):
    """
    The Amazon Resource Name (ARN) of the entity.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the WebACL that helps with identification.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier of the WebACL.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAFv2 Web ACL.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies whether this is for an AWS CloudFront distribution or for a regional applicatio
    n. Valid values are `CLOUDFRONT` or `REGIONAL`. To work with CloudFront, you must also specify the r
    egion `us-east-1` (N. Virginia) on the AWS provider.
    """
    scope: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        scope: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsV2WebAcl.Args(
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        scope: str | core.StringOut = core.arg()
