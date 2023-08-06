import terrascript.core as core


@core.resource(type="aws_kms_key", namespace="kms")
class Key(core.Resource):
    """
    The Amazon Resource Name (ARN) of the key.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A flag to indicate whether to bypass the key policy lockout safety check.
    """
    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether the key contains a symmetric key or an asymmetric key pair and the encr
    yption algorithms or signing algorithms that the key supports.
    """
    customer_master_key_spec: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The waiting period, specified in number of days. After the waiting period ends, AWS KMS d
    eletes the KMS key.
    """
    deletion_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The description of the key as viewed in AWS console.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rot
    ate-keys.html) is enabled. Defaults to false.
    """
    enable_key_rotation: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether the key is enabled. Defaults to `true`.
    """
    is_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The globally unique identifier for the key.
    """
    key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the intended use of the key. Valid values: `ENCRYPT_DECRYPT` or `SIGN_VERIFY`.
    """
    key_usage: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defau
    lts to `false`.
    """
    multi_region: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) A valid policy JSON document. Although this is a key policy, not an IAM policy, an [`aws_
    iam_policy_document`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources
    /iam_policy_document), in the form that designates a principal, can be used. For more information ab
    out building policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.
    hashicorp.com/terraform/aws/iam-policy).
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the object. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = None,
        customer_master_key_spec: str | core.StringOut | None = None,
        deletion_window_in_days: int | core.IntOut | None = None,
        description: str | core.StringOut | None = None,
        enable_key_rotation: bool | core.BoolOut | None = None,
        is_enabled: bool | core.BoolOut | None = None,
        key_usage: str | core.StringOut | None = None,
        multi_region: bool | core.BoolOut | None = None,
        policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Key.Args(
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                customer_master_key_spec=customer_master_key_spec,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enable_key_rotation=enable_key_rotation,
                is_enabled=is_enabled,
                key_usage=key_usage,
                multi_region=multi_region,
                policy=policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.arg(default=None)

        customer_master_key_spec: str | core.StringOut | None = core.arg(default=None)

        deletion_window_in_days: int | core.IntOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        enable_key_rotation: bool | core.BoolOut | None = core.arg(default=None)

        is_enabled: bool | core.BoolOut | None = core.arg(default=None)

        key_usage: str | core.StringOut | None = core.arg(default=None)

        multi_region: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
