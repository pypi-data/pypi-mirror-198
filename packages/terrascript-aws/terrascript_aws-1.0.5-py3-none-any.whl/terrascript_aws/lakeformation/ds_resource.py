import terrascript.core as core


@core.data(type="aws_lakeformation_resource", namespace="lakeformation")
class DsResource(core.Data):

    arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time the resource was last modified in [RFC 3339 format](https://tools.ietf.org/html/rf
    c3339#section-5.8).
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsResource.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()
