import terrascript.core as core


@core.data(type="aws_iam_session_context", namespace="iam")
class DsSessionContext(core.Data):

    arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    issuer_arn: str | core.StringOut = core.attr(str, computed=True)

    issuer_id: str | core.StringOut = core.attr(str, computed=True)

    issuer_name: str | core.StringOut = core.attr(str, computed=True)

    session_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsSessionContext.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()
