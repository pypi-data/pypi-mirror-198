import terrascript.core as core


@core.resource(type="aws_imagebuilder_component", namespace="aws_imagebuilder")
class Component(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    change_description: str | core.StringOut | None = core.attr(str, default=None)

    data: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    date_created: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    owner: str | core.StringOut = core.attr(str, computed=True)

    platform: str | core.StringOut = core.attr(str)

    supported_os_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    uri: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        platform: str | core.StringOut,
        version: str | core.StringOut,
        change_description: str | core.StringOut | None = None,
        data: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        supported_os_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Component.Args(
                name=name,
                platform=platform,
                version=version,
                change_description=change_description,
                data=data,
                description=description,
                kms_key_id=kms_key_id,
                supported_os_versions=supported_os_versions,
                tags=tags,
                tags_all=tags_all,
                uri=uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        change_description: str | core.StringOut | None = core.arg(default=None)

        data: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        platform: str | core.StringOut = core.arg()

        supported_os_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        uri: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()
