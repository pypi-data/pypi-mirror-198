import terrascript.core as core


@core.schema
class Condition(core.Schema):

    key: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Condition.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_cloudwatch_event_permission", namespace="aws_eventbridge")
class CloudwatchEventPermission(core.Resource):

    action: str | core.StringOut | None = core.attr(str, default=None)

    condition: Condition | None = core.attr(Condition, default=None)

    event_bus_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    principal: str | core.StringOut = core.attr(str)

    statement_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        principal: str | core.StringOut,
        statement_id: str | core.StringOut,
        action: str | core.StringOut | None = None,
        condition: Condition | None = None,
        event_bus_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventPermission.Args(
                principal=principal,
                statement_id=statement_id,
                action=action,
                condition=condition,
                event_bus_name=event_bus_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: str | core.StringOut | None = core.arg(default=None)

        condition: Condition | None = core.arg(default=None)

        event_bus_name: str | core.StringOut | None = core.arg(default=None)

        principal: str | core.StringOut = core.arg()

        statement_id: str | core.StringOut = core.arg()
