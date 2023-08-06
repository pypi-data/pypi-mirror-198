import terrascript.core as core


@core.schema
class Scope(core.Schema):

    scope_description: str | core.StringOut = core.attr(str)

    scope_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        scope_description: str | core.StringOut,
        scope_name: str | core.StringOut,
    ):
        super().__init__(
            args=Scope.Args(
                scope_description=scope_description,
                scope_name=scope_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scope_description: str | core.StringOut = core.arg()

        scope_name: str | core.StringOut = core.arg()


@core.resource(type="aws_cognito_resource_server", namespace="cognito")
class ResourceServer(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    identifier: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    scope: list[Scope] | core.ArrayOut[Scope] | None = core.attr(
        Scope, default=None, kind=core.Kind.array
    )

    scope_identifiers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        identifier: str | core.StringOut,
        name: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        scope: list[Scope] | core.ArrayOut[Scope] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceServer.Args(
                identifier=identifier,
                name=name,
                user_pool_id=user_pool_id,
                scope=scope,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identifier: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        scope: list[Scope] | core.ArrayOut[Scope] | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()
