import terrascript.core as core


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


@core.resource(type="aws_secretsmanager_secret_rotation", namespace="secretsmanager")
class SecretRotation(core.Resource):
    """
    Amazon Resource Name (ARN) of the secret.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether automatic rotation is enabled for this secret.
    """
    rotation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) Specifies the ARN of the Lambda function that can rotate the secret.
    """
    rotation_lambda_arn: str | core.StringOut = core.attr(str)

    """
    (Required) A structure that defines the rotation configuration for this secret. Defined below.
    """
    rotation_rules: RotationRules = core.attr(RotationRules)

    """
    (Required) Specifies the secret to which you want to add a new version. You can specify either the A
    mazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
    """
    secret_id: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        rotation_lambda_arn: str | core.StringOut,
        rotation_rules: RotationRules,
        secret_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecretRotation.Args(
                rotation_lambda_arn=rotation_lambda_arn,
                rotation_rules=rotation_rules,
                secret_id=secret_id,
                tags=tags,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        rotation_lambda_arn: str | core.StringOut = core.arg()

        rotation_rules: RotationRules = core.arg()

        secret_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
