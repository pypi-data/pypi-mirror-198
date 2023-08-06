import terrascript.core as core


@core.resource(type="aws_organizations_delegated_administrator", namespace="organizations")
class DelegatedAdministrator(core.Resource):
    """
    (Required) The account ID number of the member account in the organization to register as a delegate
    d administrator.
    """

    account_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the delegated administrator's account.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the account was made a delegated administrator.
    """
    delegation_enabled_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The email address that is associated with the delegated administrator's AWS account.
    """
    email: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier (ID) of the delegated administrator.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The method by which the delegated administrator's account joined the organization.
    """
    joined_method: str | core.StringOut = core.attr(str, computed=True)

    """
    The date when the delegated administrator's account became a part of the organization.
    """
    joined_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    The friendly name of the delegated administrator's account.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The service principal of the AWS service for which you want to make the member account a
    delegated administrator.
    """
    service_principal: str | core.StringOut = core.attr(str)

    """
    The status of the delegated administrator's account in the organization.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        service_principal: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DelegatedAdministrator.Args(
                account_id=account_id,
                service_principal=service_principal,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        service_principal: str | core.StringOut = core.arg()
