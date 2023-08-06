import terrascript.core as core


@core.resource(type="aws_organizations_account", namespace="organizations")
class Account(core.Resource):
    """
    The ARN for this account.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If true, a deletion event will close the account. Otherwise, it will only remove from the
    organization. This is not supported for GovCloud accounts.
    """
    close_on_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether to also create a GovCloud account. The GovCloud account is tied to the main (comm
    ercial) account this resource creates. If `true`, the GovCloud account ID is available in the `govcl
    oud_id` attribute. The only way to manage the GovCloud account with Terraform is to subsequently imp
    ort the account using this resource.
    """
    create_govcloud: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Email address of the owner to assign to the new member account. This email address must n
    ot already be associated with another AWS account.
    """
    email: str | core.StringOut = core.attr(str)

    """
    ID for a GovCloud account created with the account.
    """
    govcloud_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If set to `ALLOW`, the new account enables IAM users and roles to access account billing
    information if they have the required permissions. If set to `DENY`, then only the root user (and no
    roles) of the new account can access account billing information. If this is unset, the AWS API wil
    l default this to `ALLOW`. If the resource is created and this option is changed, it will try to rec
    reate the account.
    """
    iam_user_access_to_billing: str | core.StringOut | None = core.attr(str, default=None)

    """
    The AWS account id
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    joined_method: str | core.StringOut = core.attr(str, computed=True)

    joined_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Friendly name for the member account.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization de
    fault Root ID. A configuration must be present for this argument to perform drift detection.
    """
    parent_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The name of an IAM role that Organizations automatically preconfigures in the new member
    account. This role trusts the root account, allowing users in the root account to assume the role, a
    s permitted by the root account administrator. The role has administrator permissions in the new mem
    ber account. The Organizations API provides no method for reading this information after account cre
    ation, so Terraform cannot perform drift detection on its value and will always show a difference fo
    r a configured value after import unless [`ignore_changes`](https://www.terraform.io/docs/configurat
    ion/meta-arguments/lifecycle.html#ignore_changes) is used.
    """
    role_name: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        email: str | core.StringOut,
        name: str | core.StringOut,
        close_on_deletion: bool | core.BoolOut | None = None,
        create_govcloud: bool | core.BoolOut | None = None,
        iam_user_access_to_billing: str | core.StringOut | None = None,
        parent_id: str | core.StringOut | None = None,
        role_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                email=email,
                name=name,
                close_on_deletion=close_on_deletion,
                create_govcloud=create_govcloud,
                iam_user_access_to_billing=iam_user_access_to_billing,
                parent_id=parent_id,
                role_name=role_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        close_on_deletion: bool | core.BoolOut | None = core.arg(default=None)

        create_govcloud: bool | core.BoolOut | None = core.arg(default=None)

        email: str | core.StringOut = core.arg()

        iam_user_access_to_billing: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parent_id: str | core.StringOut | None = core.arg(default=None)

        role_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
