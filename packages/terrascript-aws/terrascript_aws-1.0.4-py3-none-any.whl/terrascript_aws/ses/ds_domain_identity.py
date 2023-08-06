import terrascript.core as core


@core.data(type="aws_ses_domain_identity", namespace="ses")
class DsDomainIdentity(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    verification_token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        domain: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDomainIdentity.Args(
                domain=domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: str | core.StringOut = core.arg()
