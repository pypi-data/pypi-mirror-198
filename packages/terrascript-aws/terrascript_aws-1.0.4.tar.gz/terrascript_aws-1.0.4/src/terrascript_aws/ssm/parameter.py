import terrascript.core as core


@core.resource(type="aws_ssm_parameter", namespace="ssm")
class Parameter(core.Resource):
    """
    (Optional) Regular expression used to validate the parameter value.
    """

    allowed_pattern: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of the parameter.
    """
    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Data type of the parameter. Valid values: `text` and `aws:ec2:image` for AMI format, see
    the [Native parameter support for Amazon Machine Image IDs](https://docs.aws.amazon.com/systems-mana
    ger/latest/userguide/parameter-store-ec2-aliases.html).
    """
    data_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Description of the parameter.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, exactly one of `value` or `insecure_value` is required) Value of the parameter. **Use cau
    tion:** This value is _never_ marked as sensitive in the Terraform plan output. This argument is not
    valid with a `type` of `SecureString`.
    """
    insecure_value: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) KMS key ID or ARN for encrypting a SecureString.
    """
    key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Name of the parameter. If the name contains a path (e.g., any forward slashes (`/`)), it
    must be fully qualified with a leading forward slash (`/`). For additional requirements and constrai
    nts, see the [AWS SSM User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysma
    n-parameter-name-constraints.html).
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Overwrite an existing parameter. If not specified, will default to `false` if the resourc
    e has not been created by terraform to avoid overwrite of existing resource and will default to `tru
    e` otherwise (terraform lifecycle rules should then be used to manage the update behavior).
    """
    overwrite: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Map of tags to assign to the object. If configured with a provider [`default_tags` config
    uration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-config
    uration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Parameter tier to assign to the parameter. If not specified, will use the default paramet
    er tier for the region. Valid tiers are `Standard`, `Advanced`, and `Intelligent-Tiering`. Downgradi
    ng an `Advanced` tier parameter to `Standard` will recreate the resource. For more information on pa
    rameter tiers, see the [AWS SSM Parameter tier comparison and guide](https://docs.aws.amazon.com/sys
    tems-manager/latest/userguide/parameter-store-advanced-parameters.html).
    """
    tier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Type of the parameter. Valid types are `String`, `StringList` and `SecureString`.
    """
    type: str | core.StringOut = core.attr(str)

    """
    (Optional, exactly one of `value` or `insecure_value` is required) Value of the parameter. This valu
    e is always marked as sensitive in the Terraform plan output, regardless of `type`. In Terraform CLI
    version 0.15 and later, this may require additional configuration handling for certain scenarios. F
    or more information, see the [Terraform v0.15 Upgrade Guide](https://www.terraform.io/upgrade-guides
    /0-15.html#sensitive-output-values).
    """
    value: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Version of the parameter.
    """
    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        allowed_pattern: str | core.StringOut | None = None,
        arn: str | core.StringOut | None = None,
        data_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        insecure_value: str | core.StringOut | None = None,
        key_id: str | core.StringOut | None = None,
        overwrite: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tier: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Parameter.Args(
                name=name,
                type=type,
                allowed_pattern=allowed_pattern,
                arn=arn,
                data_type=data_type,
                description=description,
                insecure_value=insecure_value,
                key_id=key_id,
                overwrite=overwrite,
                tags=tags,
                tags_all=tags_all,
                tier=tier,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_pattern: str | core.StringOut | None = core.arg(default=None)

        arn: str | core.StringOut | None = core.arg(default=None)

        data_type: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        insecure_value: str | core.StringOut | None = core.arg(default=None)

        key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        overwrite: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tier: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut | None = core.arg(default=None)
