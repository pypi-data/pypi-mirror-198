import terrascript.core as core


@core.data(type="aws_wafv2_web_acl", namespace="aws_waf")
class DsV2WebAcl(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

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
