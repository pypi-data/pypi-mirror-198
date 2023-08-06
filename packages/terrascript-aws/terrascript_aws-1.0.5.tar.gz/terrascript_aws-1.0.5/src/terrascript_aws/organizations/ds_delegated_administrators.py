import terrascript.core as core


@core.schema
class DelegatedAdministratorsBlk(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    delegation_enabled_date: str | core.StringOut = core.attr(str, computed=True)

    email: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    joined_method: str | core.StringOut = core.attr(str, computed=True)

    joined_timestamp: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        delegation_enabled_date: str | core.StringOut,
        email: str | core.StringOut,
        id: str | core.StringOut,
        joined_method: str | core.StringOut,
        joined_timestamp: str | core.StringOut,
        name: str | core.StringOut,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=DelegatedAdministratorsBlk.Args(
                arn=arn,
                delegation_enabled_date=delegation_enabled_date,
                email=email,
                id=id,
                joined_method=joined_method,
                joined_timestamp=joined_timestamp,
                name=name,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        delegation_enabled_date: str | core.StringOut = core.arg()

        email: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        joined_method: str | core.StringOut = core.arg()

        joined_timestamp: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()


@core.data(type="aws_organizations_delegated_administrators", namespace="organizations")
class DsDelegatedAdministrators(core.Data):
    """
    The list of delegated administrators in your organization, which have the following attributes:
    """

    delegated_administrators: list[DelegatedAdministratorsBlk] | core.ArrayOut[
        DelegatedAdministratorsBlk
    ] = core.attr(DelegatedAdministratorsBlk, computed=True, kind=core.Kind.array)

    """
    The unique identifier (ID) of the delegated administrator's account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies a service principal name. If specified, then the operation lists the delegated
    administrators only for the specified service. If you don't specify a service principal, the operati
    on lists all delegated administrators for all services in your organization.
    """
    service_principal: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        service_principal: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDelegatedAdministrators.Args(
                service_principal=service_principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        service_principal: str | core.StringOut | None = core.arg(default=None)
