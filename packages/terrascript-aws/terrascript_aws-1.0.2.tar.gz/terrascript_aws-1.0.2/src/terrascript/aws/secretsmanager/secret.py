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


@core.resource(type="aws_secretsmanager_secret", namespace="aws_secretsmanager")
class Secret(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    force_overwrite_replica_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    recovery_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    replica: list[Replica] | core.ArrayOut[Replica] | None = core.attr(
        Replica, default=None, computed=True, kind=core.Kind.array
    )

    rotation_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    rotation_lambda_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    rotation_rules: RotationRules | None = core.attr(RotationRules, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
