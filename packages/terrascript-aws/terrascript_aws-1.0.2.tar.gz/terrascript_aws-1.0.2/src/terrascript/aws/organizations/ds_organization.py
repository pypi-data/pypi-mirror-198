import terrascript.core as core


@core.schema
class NonMasterAccounts(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    email: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        email: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=NonMasterAccounts.Args(
                arn=arn,
                email=email,
                id=id,
                name=name,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        email: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()


@core.schema
class PolicyTypes(core.Schema):

    status: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=PolicyTypes.Args(
                status=status,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class Roots(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    policy_types: list[PolicyTypes] | core.ArrayOut[PolicyTypes] = core.attr(
        PolicyTypes, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
        policy_types: list[PolicyTypes] | core.ArrayOut[PolicyTypes],
    ):
        super().__init__(
            args=Roots.Args(
                arn=arn,
                id=id,
                name=name,
                policy_types=policy_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        policy_types: list[PolicyTypes] | core.ArrayOut[PolicyTypes] = core.arg()


@core.schema
class Accounts(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    email: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        email: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=Accounts.Args(
                arn=arn,
                email=email,
                id=id,
                name=name,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        email: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()


@core.data(type="aws_organizations_organization", namespace="aws_organizations")
class DsOrganization(core.Data):

    accounts: list[Accounts] | core.ArrayOut[Accounts] = core.attr(
        Accounts, computed=True, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_service_access_principals: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    enabled_policy_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    feature_set: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    master_account_arn: str | core.StringOut = core.attr(str, computed=True)

    master_account_email: str | core.StringOut = core.attr(str, computed=True)

    master_account_id: str | core.StringOut = core.attr(str, computed=True)

    non_master_accounts: list[NonMasterAccounts] | core.ArrayOut[NonMasterAccounts] = core.attr(
        NonMasterAccounts, computed=True, kind=core.Kind.array
    )

    roots: list[Roots] | core.ArrayOut[Roots] = core.attr(
        Roots, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsOrganization.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
