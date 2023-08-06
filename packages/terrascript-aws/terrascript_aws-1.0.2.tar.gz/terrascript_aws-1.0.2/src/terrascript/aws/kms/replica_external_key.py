import terrascript.core as core


@core.resource(type="aws_kms_replica_external_key", namespace="aws_kms")
class ReplicaExternalKey(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    deletion_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    expiration_model: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_id: str | core.StringOut = core.attr(str, computed=True)

    key_material_base64: str | core.StringOut | None = core.attr(str, default=None)

    key_state: str | core.StringOut = core.attr(str, computed=True)

    key_usage: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    primary_key_arn: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    valid_to: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        primary_key_arn: str | core.StringOut,
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = None,
        deletion_window_in_days: int | core.IntOut | None = None,
        description: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        key_material_base64: str | core.StringOut | None = None,
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
            args=ReplicaExternalKey.Args(
                primary_key_arn=primary_key_arn,
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                deletion_window_in_days=deletion_window_in_days,
                description=description,
                enabled=enabled,
                key_material_base64=key_material_base64,
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

        policy: str | core.StringOut | None = core.arg(default=None)

        primary_key_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        valid_to: str | core.StringOut | None = core.arg(default=None)
