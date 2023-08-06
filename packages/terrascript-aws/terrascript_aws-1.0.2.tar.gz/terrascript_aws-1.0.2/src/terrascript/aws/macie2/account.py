import terrascript.core as core


@core.resource(type="aws_macie2_account", namespace="aws_macie2")
class Account(core.Resource):

    created_at: str | core.StringOut = core.attr(str, computed=True)

    finding_publishing_frequency: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    service_role: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        finding_publishing_frequency: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                finding_publishing_frequency=finding_publishing_frequency,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        finding_publishing_frequency: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)
