import terrascript.core as core


@core.resource(type="aws_iot_thing", namespace="aws_iot")
class Thing(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    default_client_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    thing_type_name: str | core.StringOut | None = core.attr(str, default=None)

    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        thing_type_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Thing.Args(
                name=name,
                attributes=attributes,
                thing_type_name=thing_type_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        thing_type_name: str | core.StringOut | None = core.arg(default=None)
