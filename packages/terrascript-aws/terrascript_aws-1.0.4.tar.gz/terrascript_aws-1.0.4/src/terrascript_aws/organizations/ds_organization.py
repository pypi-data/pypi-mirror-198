import terrascript.core as core


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


@core.data(type="aws_organizations_organization", namespace="organizations")
class DsOrganization(core.Data):
    """
    List of organization accounts including the master account. For a list excluding the master account,
    see the `non_master_accounts` attribute. All elements have these attributes:
    """

    accounts: list[Accounts] | core.ArrayOut[Accounts] = core.attr(
        Accounts, computed=True, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) of the organization.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of AWS service principal names that have integration enabled with your organization. Organiza
    tion must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations Us
    er Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
    """
    aws_service_access_principals: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A list of Organizations policy types that are enabled in the Organization Root. Organization must ha
    ve `feature_set` set to `ALL`. For additional information about valid policy types (e.g., `SERVICE_C
    ONTROL_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations
    /latest/APIReference/API_EnablePolicyType.html).
    """
    enabled_policy_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The FeatureSet of the organization.
    """
    feature_set: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the organization.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the account that is designated as the master account for the organ
    ization.
    """
    master_account_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The email address that is associated with the AWS account that is designated as the master account f
    or the organization.
    """
    master_account_email: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier (ID) of the master account of an organization.
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
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsOrganization.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
