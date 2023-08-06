import terrascript.core as core


@core.schema
class StorageConnectors(core.Schema):

    connector_type: str | core.StringOut = core.attr(str)

    domains: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    resource_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        connector_type: str | core.StringOut,
        domains: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resource_identifier: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StorageConnectors.Args(
                connector_type=connector_type,
                domains=domains,
                resource_identifier=resource_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connector_type: str | core.StringOut = core.arg()

        domains: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        resource_identifier: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AccessEndpoints(core.Schema):

    endpoint_type: str | core.StringOut = core.attr(str)

    vpce_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        endpoint_type: str | core.StringOut,
        vpce_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AccessEndpoints.Args(
                endpoint_type=endpoint_type,
                vpce_id=vpce_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_type: str | core.StringOut = core.arg()

        vpce_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ApplicationSettings(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    settings_group: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        settings_group: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ApplicationSettings.Args(
                enabled=enabled,
                settings_group=settings_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        settings_group: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UserSettings(core.Schema):

    action: str | core.StringOut = core.attr(str)

    permission: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action: str | core.StringOut,
        permission: str | core.StringOut,
    ):
        super().__init__(
            args=UserSettings.Args(
                action=action,
                permission=permission,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()

        permission: str | core.StringOut = core.arg()


@core.resource(type="aws_appstream_stack", namespace="appstream")
class Stack(core.Resource):
    """
    (Optional) Set of configuration blocks defining the interface VPC endpoints. Users of the stack can
    connect to AppStream 2.0 only through the specified endpoints. See below.
    """

    access_endpoints: list[AccessEndpoints] | core.ArrayOut[AccessEndpoints] | None = core.attr(
        AccessEndpoints, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Settings for application settings persistence.
    """
    application_settings: ApplicationSettings | None = core.attr(
        ApplicationSettings, default=None, computed=True
    )

    """
    ARN of the appstream stack.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time, in UTC and extended RFC 3339 format, when the stack was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description for the AppStream stack.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Stack name to display.
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must app
    rove the domains that you want to host embedded AppStream 2.0 streaming sessions.
    """
    embed_host_domains: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) URL that users are redirected to after they click the Send Feedback link. If no URL is sp
    ecified, no Send Feedback link is displayed. .
    """
    feedback_url: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Unique ID of the appstream stack.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique name for the AppStream stack.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) URL that users are redirected to after their streaming session ends.
    """
    redirect_url: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for the storage connectors to enable. See below.
    """
    storage_connectors: list[StorageConnectors] | core.ArrayOut[
        StorageConnectors
    ] | None = core.attr(StorageConnectors, default=None, computed=True, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Configuration block for the actions that are enabled or disabled for users during their s
    treaming sessions. By default, these actions are enabled. See below.
    """
    user_settings: list[UserSettings] | core.ArrayOut[UserSettings] | None = core.attr(
        UserSettings, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        access_endpoints: list[AccessEndpoints] | core.ArrayOut[AccessEndpoints] | None = None,
        application_settings: ApplicationSettings | None = None,
        description: str | core.StringOut | None = None,
        display_name: str | core.StringOut | None = None,
        embed_host_domains: list[str] | core.ArrayOut[core.StringOut] | None = None,
        feedback_url: str | core.StringOut | None = None,
        redirect_url: str | core.StringOut | None = None,
        storage_connectors: list[StorageConnectors]
        | core.ArrayOut[StorageConnectors]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_settings: list[UserSettings] | core.ArrayOut[UserSettings] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stack.Args(
                name=name,
                access_endpoints=access_endpoints,
                application_settings=application_settings,
                description=description,
                display_name=display_name,
                embed_host_domains=embed_host_domains,
                feedback_url=feedback_url,
                redirect_url=redirect_url,
                storage_connectors=storage_connectors,
                tags=tags,
                tags_all=tags_all,
                user_settings=user_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_endpoints: list[AccessEndpoints] | core.ArrayOut[AccessEndpoints] | None = core.arg(
            default=None
        )

        application_settings: ApplicationSettings | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        embed_host_domains: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        feedback_url: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        redirect_url: str | core.StringOut | None = core.arg(default=None)

        storage_connectors: list[StorageConnectors] | core.ArrayOut[
            StorageConnectors
        ] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_settings: list[UserSettings] | core.ArrayOut[UserSettings] | None = core.arg(
            default=None
        )
