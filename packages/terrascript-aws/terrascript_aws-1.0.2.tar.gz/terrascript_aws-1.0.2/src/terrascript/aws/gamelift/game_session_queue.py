import terrascript.core as core


@core.schema
class PlayerLatencyPolicy(core.Schema):

    maximum_individual_player_latency_milliseconds: int | core.IntOut = core.attr(int)

    policy_duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        maximum_individual_player_latency_milliseconds: int | core.IntOut,
        policy_duration_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=PlayerLatencyPolicy.Args(
                maximum_individual_player_latency_milliseconds=maximum_individual_player_latency_milliseconds,
                policy_duration_seconds=policy_duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_individual_player_latency_milliseconds: int | core.IntOut = core.arg()

        policy_duration_seconds: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_gamelift_game_session_queue", namespace="aws_gamelift")
class GameSessionQueue(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    notification_target: str | core.StringOut | None = core.attr(str, default=None)

    player_latency_policy: list[PlayerLatencyPolicy] | core.ArrayOut[
        PlayerLatencyPolicy
    ] | None = core.attr(PlayerLatencyPolicy, default=None, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        destinations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        notification_target: str | core.StringOut | None = None,
        player_latency_policy: list[PlayerLatencyPolicy]
        | core.ArrayOut[PlayerLatencyPolicy]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout_in_seconds: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GameSessionQueue.Args(
                name=name,
                destinations=destinations,
                notification_target=notification_target,
                player_latency_policy=player_latency_policy,
                tags=tags,
                tags_all=tags_all,
                timeout_in_seconds=timeout_in_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        notification_target: str | core.StringOut | None = core.arg(default=None)

        player_latency_policy: list[PlayerLatencyPolicy] | core.ArrayOut[
            PlayerLatencyPolicy
        ] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)
