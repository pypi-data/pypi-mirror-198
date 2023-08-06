import terrascript.core as core


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


@core.resource(type="aws_organizations_organization", namespace="organizations")
class Organization(core.Resource):
    """
    List of organization accounts including the master account. For a list excluding the master account,
    see the `non_master_accounts` attribute. All elements have these attributes:
    """

    accounts: list[Accounts] | core.ArrayOut[Accounts] = core.attr(
        Accounts, computed=True, kind=core.Kind.array
    )

    """
    ARN of the account
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of AWS service principal names for which you want to enable integration with your or
    ganization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Orga
    nization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organization
    s User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.htm
    l).
    """
    aws_service_access_principals: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of Organizations policy types to enable in the Organization Root. Organization must
    have `feature_set` set to `ALL`. For additional information about valid policy types (e.g., `AISERVI
    CES_OPT_OUT_POLICY`, `BACKUP_POLICY`, `SERVICE_CONTROL_POLICY`, and `TAG_POLICY`), see the [AWS Orga
    nizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePol
    icyType.html).
    """
    enabled_policy_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Specify "ALL" (default) or "CONSOLIDATED_BILLING".
    """
    feature_set: str | core.StringOut | None = core.attr(str, default=None)

    """
    Identifier of the account
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the master account
    """
    master_account_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Email address of the master account
    """
    master_account_email: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the master account
    """
    master_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of organization accounts excluding the master account. For a list including the master account,
    see the `accounts` attribute. All elements have these attributes:
    """
    non_master_accounts: list[NonMasterAccounts] | core.ArrayOut[NonMasterAccounts] = core.attr(
        NonMasterAccounts, computed=True, kind=core.Kind.array
    )

    """
    List of organization roots. All elements have these attributes:
    """
    roots: list[Roots] | core.ArrayOut[Roots] = core.attr(
        Roots, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        aws_service_access_principals: list[str] | core.ArrayOut[core.StringOut] | None = None,
        enabled_policy_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        feature_set: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Organization.Args(
                aws_service_access_principals=aws_service_access_principals,
                enabled_policy_types=enabled_policy_types,
                feature_set=feature_set,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_service_access_principals: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        enabled_policy_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        feature_set: str | core.StringOut | None = core.arg(default=None)
