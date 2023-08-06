import terrascript.core as core


@core.schema
class Target(core.Schema):

    id: str | core.StringOut = core.attr(str)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Target.Args(
                id=id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_directory_service_shared_directory", namespace="aws_ds")
class DirectoryServiceSharedDirectory(core.Resource):

    directory_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    method: str | core.StringOut | None = core.attr(str, default=None)

    notes: str | core.StringOut | None = core.attr(str, default=None)

    shared_directory_id: str | core.StringOut = core.attr(str, computed=True)

    target: Target = core.attr(Target)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: str | core.StringOut,
        target: Target,
        method: str | core.StringOut | None = None,
        notes: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceSharedDirectory.Args(
                directory_id=directory_id,
                target=target,
                method=method,
                notes=notes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: str | core.StringOut = core.arg()

        method: str | core.StringOut | None = core.arg(default=None)

        notes: str | core.StringOut | None = core.arg(default=None)

        target: Target = core.arg()
