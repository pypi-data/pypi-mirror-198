import terrascript.core as core


@core.resource(type="aws_kms_replica_key", namespace="kms")
class ReplicaKey(core.Resource):
    """
    The Amazon Resource Name (ARN) of the replica key. The key ARNs of related multi-Region keys differ
    only in the Region value.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A flag to indicate whether to bypass the key policy lockout safety check.
    """
    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The waiting period, specified in number of days. After the waiting period ends, AWS KMS d
    eletes the KMS key.
    """
    deletion_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A description of the KMS key.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether the replica key is enabled. Disabled KMS keys cannot be used in cryptog
    raphic operations. The default value is `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The key ID of the replica key. Related multi-Region keys have the same key ID.
    """
    key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A Boolean value that specifies whether key rotation is enabled. This is a shared property of multi-R
    egion keys.
    """
    key_rotation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The type of key material in the KMS key. This is a shared property of multi-Region keys.
    """
    key_spec: str | core.StringOut = core.attr(str, computed=True)

    """
    The [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#c
    ryptographic-operations) for which you can use the KMS key. This is a shared property of multi-Regio
    n keys.
    """
    key_usage: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The key policy to attach to the KMS key. If you do not specify a key policy, AWS KMS atta
    ches the [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.htm
    l#key-policy-default) to the KMS key.
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The ARN of the multi-Region primary key to replicate. The primary key must be in a differ
    ent AWS Region of the same AWS Partition. You can create only one replica of a given primary key in
    each AWS Region.
    """
    primary_key_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the replica key. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
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
        primary_key_arn: str | core.StringOut,
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = None,
        deletion_window_in_days: int | core.IntOut | None = None,
        description: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicaKey.Args(
                primary_key_arn=primary_key_arn,
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enabled=enabled,
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

        deletion_window_in_days: int | core.IntOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        primary_key_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
