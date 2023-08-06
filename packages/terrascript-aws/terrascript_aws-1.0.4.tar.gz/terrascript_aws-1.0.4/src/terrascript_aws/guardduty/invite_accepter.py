import terrascript.core as core


@core.resource(type="aws_guardduty_invite_accepter", namespace="guardduty")
class InviteAccepter(core.Resource):
    """
    (Required) The detector ID of the member GuardDuty account.
    """

    detector_id: str | core.StringOut = core.attr(str)

    """
    GuardDuty member detector ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) AWS account ID for primary account.
    """
    master_account_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        detector_id: str | core.StringOut,
        master_account_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InviteAccepter.Args(
                detector_id=detector_id,
                master_account_id=master_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        detector_id: str | core.StringOut = core.arg()

        master_account_id: str | core.StringOut = core.arg()
