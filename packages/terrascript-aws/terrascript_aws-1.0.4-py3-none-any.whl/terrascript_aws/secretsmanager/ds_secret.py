import terrascript.core as core


@core.schema
class RotationRules(core.Schema):

    automatically_after_days: int | core.IntOut = core.attr(int, computed=True)

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


@core.data(type="aws_secretsmanager_secret", namespace="secretsmanager")
class DsSecret(core.Data):
    """
    (Optional) The Amazon Resource Name (ARN) of the secret to retrieve.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    A description of the secret.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the secret.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the secret to retrieve.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The resource-based policy document that's attached to the secret.
    """
    policy: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether rotation is enabled or not.
    """
    rotation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Rotation Lambda function Amazon Resource Name (ARN) if rotation is enabled.
    """
    rotation_lambda_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Rotation rules if rotation is enabled.
    """
    rotation_rules: list[RotationRules] | core.ArrayOut[RotationRules] = core.attr(
        RotationRules, computed=True, kind=core.Kind.array
    )

    """
    Tags of the secret.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSecret.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
