import terrascript.core as core


@core.schema
class Replica(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    last_accessed_date: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    status_message: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        last_accessed_date: str | core.StringOut,
        region: str | core.StringOut,
        status: str | core.StringOut,
        status_message: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Replica.Args(
                last_accessed_date=last_accessed_date,
                region=region,
                status=status,
                status_message=status_message,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        last_accessed_date: str | core.StringOut = core.arg()

        region: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

        status_message: str | core.StringOut = core.arg()


@core.schema
class RotationRules(core.Schema):

    automatically_after_days: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        automatically_after_days: int | core.IntOut,
    ):
        super().__init__(
            args=RotationRules.Args(
                automatically_after_days=automatically_after_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        automatically_after_days: int | core.IntOut = core.arg()


@core.resource(type="aws_secretsmanager_secret", namespace="secretsmanager")
class Secret(core.Resource):
    """
    ARN of the secret.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the secret.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Accepts boolean value to specify whether to overwrite a secret with the same name in the
    destination Region.
    """
    force_overwrite_replica_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    ARN of the secret.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN or Id of the AWS KMS key to be used to encrypt the secret values in the versions stor
    ed in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS a
    ccount's default KMS key (the one named `aws/secretsmanager`). If the default KMS key with that name
    doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Friendly name of the new secret. The secret name can consist of uppercase letters, lowerc
    ase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsm
    anager/latest/userguide/auth-and-access_resource-based-policies.html). For more information about bu
    ilding AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://lear
    n.hashicorp.com/terraform/aws/iam-policy). Removing `policy` from your configuration or setting `pol
    icy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could ha
    ve been set by `aws_secretsmanager_secret_policy`. To delete the `policy`, set it to `"{}"` (an empt
    y JSON document).
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Number of days that AWS Secrets Manager waits before it can delete the secret. This value
    can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is
    30`.
    """
    recovery_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Configuration block to support secret replication. See details below.
    """
    replica: list[Replica] | core.ArrayOut[Replica] | None = core.attr(
        Replica, default=None, computed=True, kind=core.Kind.array
    )

    """
    Whether automatic rotation is enabled for this secret.
    """
    rotation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional, **DEPRECATED**) ARN of the Lambda function that can rotate the secret. Use the `aws_secre
    tsmanager_secret_rotation` resource to manage this configuration instead. As of version 2.67.0, remo
    val of this configuration will no longer remove rotation due to supporting the new resource. Either
    import the new resource and remove the configuration or manually remove rotation.
    """
    rotation_lambda_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, **DEPRECATED**) Configuration block for the rotation configuration of this secret. Define
    d below. Use the `aws_secretsmanager_secret_rotation` resource to manage this configuration instead.
    As of version 2.67.0, removal of this configuration will no longer remove rotation due to supportin
    g the new resource. Either import the new resource and remove the configuration or manually remove r
    otation.
    """
    rotation_rules: RotationRules | None = core.attr(RotationRules, default=None, computed=True)

    """
    (Optional) Key-value map of user-defined tags that are attached to the secret. If configured with a
    provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/
    latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those
    defined at the provider-level.
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

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut | None = None,
        force_overwrite_replica_secret: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        recovery_window_in_days: int | core.IntOut | None = None,
        replica: list[Replica] | core.ArrayOut[Replica] | None = None,
        rotation_lambda_arn: str | core.StringOut | None = None,
        rotation_rules: RotationRules | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Secret.Args(
                description=description,
                force_overwrite_replica_secret=force_overwrite_replica_secret,
                kms_key_id=kms_key_id,
                name=name,
                name_prefix=name_prefix,
                policy=policy,
                recovery_window_in_days=recovery_window_in_days,
                replica=replica,
                rotation_lambda_arn=rotation_lambda_arn,
                rotation_rules=rotation_rules,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        force_overwrite_replica_secret: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        recovery_window_in_days: int | core.IntOut | None = core.arg(default=None)

        replica: list[Replica] | core.ArrayOut[Replica] | None = core.arg(default=None)

        rotation_lambda_arn: str | core.StringOut | None = core.arg(default=None)

        rotation_rules: RotationRules | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
