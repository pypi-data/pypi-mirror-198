import terrascript.core as core


@core.schema
class TriggerBlk(core.Schema):

    branches: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    custom_data: str | core.StringOut | None = core.attr(str, default=None)

    destination_arn: str | core.StringOut = core.attr(str)

    events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination_arn: str | core.StringOut,
        events: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        branches: list[str] | core.ArrayOut[core.StringOut] | None = None,
        custom_data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TriggerBlk.Args(
                destination_arn=destination_arn,
                events=events,
                name=name,
                branches=branches,
                custom_data=custom_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branches: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        custom_data: str | core.StringOut | None = core.arg(default=None)

        destination_arn: str | core.StringOut = core.arg()

        events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()


@core.resource(type="aws_codecommit_trigger", namespace="codecommit")
class Trigger(core.Resource):
    """
    System-generated unique identifier.
    """

    configuration_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for the repository. This needs to be less than 100 characters.
    """
    repository_name: str | core.StringOut = core.attr(str)

    trigger: list[TriggerBlk] | core.ArrayOut[TriggerBlk] = core.attr(
        TriggerBlk, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        repository_name: str | core.StringOut,
        trigger: list[TriggerBlk] | core.ArrayOut[TriggerBlk],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Trigger.Args(
                repository_name=repository_name,
                trigger=trigger,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        repository_name: str | core.StringOut = core.arg()

        trigger: list[TriggerBlk] | core.ArrayOut[TriggerBlk] = core.arg()
