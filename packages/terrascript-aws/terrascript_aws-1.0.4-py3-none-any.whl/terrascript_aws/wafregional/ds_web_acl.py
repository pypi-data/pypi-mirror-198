import terrascript.core as core


@core.data(type="aws_wafregional_web_acl", namespace="wafregional")
class DsWebAcl(core.Data):
    """
    The ID of the WAF Regional Web ACL.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the WAF Regional Web ACL.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsWebAcl.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
