import terrascript.core as core


@core.resource(type="aws_kms_key", namespace="aws_kms")
class Key(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    customer_master_key_spec: str | core.StringOut | None = core.attr(str, default=None)

    deletion_window_in_days: int | core.IntOut | None = core.attr(int, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enable_key_rotation: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    is_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    key_id: str | core.StringOut = core.attr(str, computed=True)

    key_usage: str | core.StringOut | None = core.attr(str, default=None)

    multi_region: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
