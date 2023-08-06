import terrascript.core as core


@core.data(type="aws_iam_session_context", namespace="aws_iam")
class DsSessionContext(core.Data):
    """
    (Required) ARN for an assumed role.
    """

    arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    IAM source role ARN if `arn` corresponds to an STS assumed role. Otherwise, `issuer_arn` is equal to
    arn`.
    """
    issuer_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Unique identifier of the IAM role that issues the STS assumed role.
    """
    issuer_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the source role. Only available if `arn` corresponds to an STS assumed role.
    """
    issuer_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the STS session. Only available if `arn` corresponds to an STS assumed role.
    """
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
