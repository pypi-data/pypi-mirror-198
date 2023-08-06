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


@core.data(type="aws_secretsmanager_secret_rotation", namespace="aws_secretsmanager")
class DsSecretRotation(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    rotation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    rotation_lambda_arn: str | core.StringOut = core.attr(str, computed=True)

    rotation_rules: list[RotationRules] | core.ArrayOut[RotationRules] = core.attr(
        RotationRules, computed=True, kind=core.Kind.array
    )

    secret_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        secret_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsSecretRotation.Args(
                secret_id=secret_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret_id: str | core.StringOut = core.arg()
