import terrascript.core as core


@core.resource(type="aws_guardduty_ipset", namespace="aws_guardduty")
class Ipset(core.Resource):

    activate: bool | core.BoolOut = core.attr(bool)

    arn: str | core.StringOut = core.attr(str, computed=True)

    detector_id: str | core.StringOut = core.attr(str)

    format: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    location: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

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
        activate: bool | core.BoolOut,
        detector_id: str | core.StringOut,
        format: str | core.StringOut,
        location: str | core.StringOut,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipset.Args(
                activate=activate,
                detector_id=detector_id,
                format=format,
                location=location,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activate: bool | core.BoolOut = core.arg()

        detector_id: str | core.StringOut = core.arg()

        format: str | core.StringOut = core.arg()

        location: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
