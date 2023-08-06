import terrascript.core as core


@core.resource(type="aws_kms_external_key", namespace="kms")
class ExternalKey(core.Resource):
    """
    The Amazon Resource Name (ARN) of the key.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether to disable the policy lockout check performed when creating or updating
    the key's policy. Setting this value to `true` increases the risk that the key becomes unmanageable
    . For more information, refer to the scenario in the [Default Key Policy](https://docs.aws.amazon.co
    m/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) section in t
    he AWS Key Management Service Developer Guide. Defaults to `false`.
    """
    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Duration in days after which the key is deleted after destruction of the resource. Must b
    e between `7` and `30` days. Defaults to `30`.
    """
    deletion_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Description of the key.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether the key is enabled. Keys pending import can only be `false`. Imported k
    eys default to `true` unless expired.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    Whether the key material expires. Empty when pending key material import, otherwise `KEY_MATERIAL_EX
    PIRES` or `KEY_MATERIAL_DOES_NOT_EXPIRE`.
    """
    expiration_model: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier for the key.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Base64 encoded 256-bit symmetric encryption key material to import. The CMK is permanentl
    y associated with this key material. The same key material can be reimported, but you cannot import
    different key material.
    """
    key_material_base64: str | core.StringOut | None = core.attr(str, default=None)

    """
    The state of the CMK.
    """
    key_state: str | core.StringOut = core.attr(str, computed=True)

    """
    The cryptographic operations for which you can use the CMK.
    """
    key_usage: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether the KMS key is a multi-Region (`true`) or regional (`false`) key. Defau
    lts to `false`.
    """
    multi_region: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) A key policy JSON document. If you do not provide a key policy, AWS KMS attaches a defaul
    t key policy to the CMK.
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A key-value map of tags to assign to the key. If configured with a provider [`default_tag
    s` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_ta
    gs-configuration-block) present, tags with matching keys will overwrite those defined at the provide
    r-level.
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

    """
    (Optional) Time at which the imported key material expires. When the key material expires, AWS KMS d
    eletes the key material and the CMK becomes unusable. If not specified, key material does not expire
    . Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDT
    HH:MM:SSZ`)
    """
    valid_to: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = None,
        deletion_window_in_days: int | core.IntOut | None = None,
        description: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        key_material_base64: str | core.StringOut | None = None,
        multi_region: bool | core.BoolOut | None = None,
        policy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        valid_to: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ExternalKey.Args(
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enabled=enabled,
                key_material_base64=key_material_base64,
                multi_region=multi_region,
                policy=policy,
                tags=tags,
                tags_all=tags_all,
                valid_to=valid_to,
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

        key_material_base64: str | core.StringOut | None = core.arg(default=None)

        multi_region: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        valid_to: str | core.StringOut | None = core.arg(default=None)
