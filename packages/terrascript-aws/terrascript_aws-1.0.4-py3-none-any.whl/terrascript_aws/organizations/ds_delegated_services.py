import terrascript.core as core


@core.schema
class DelegatedServicesBlk(core.Schema):

    delegation_enabled_date: str | core.StringOut = core.attr(str, computed=True)

    service_principal: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delegation_enabled_date: str | core.StringOut,
        service_principal: str | core.StringOut,
    ):
        super().__init__(
            args=DelegatedServicesBlk.Args(
                delegation_enabled_date=delegation_enabled_date,
                service_principal=service_principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delegation_enabled_date: str | core.StringOut = core.arg()

        service_principal: str | core.StringOut = core.arg()


@core.data(type="aws_organizations_delegated_services", namespace="organizations")
class DsDelegatedServices(core.Data):
    """
    (Required) The account ID number of a delegated administrator account in the organization.
    """

    account_id: str | core.StringOut = core.attr(str)

    """
    The services for which the account is a delegated administrator, which have the following attributes
    :
    """
    delegated_services: list[DelegatedServicesBlk] | core.ArrayOut[
        DelegatedServicesBlk
    ] = core.attr(DelegatedServicesBlk, computed=True, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        account_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDelegatedServices.Args(
                account_id=account_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut = core.arg()
