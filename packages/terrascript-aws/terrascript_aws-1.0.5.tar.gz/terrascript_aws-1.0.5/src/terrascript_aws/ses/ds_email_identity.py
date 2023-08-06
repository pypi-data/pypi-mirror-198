import terrascript.core as core


@core.data(type="aws_ses_email_identity", namespace="ses")
class DsEmailIdentity(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    email: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        email: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsEmailIdentity.Args(
                email=email,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email: str | core.StringOut = core.arg()
