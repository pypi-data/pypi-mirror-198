import terrascript.core as core


@core.schema
class NotificationConfiguration(core.Schema):

    notification_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        notification_topic_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NotificationConfiguration.Args(
                notification_topic_arn=notification_topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notification_topic_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CognitoMemberDefinition(core.Schema):

    client_id: str | core.StringOut = core.attr(str)

    user_group: str | core.StringOut = core.attr(str)

    user_pool: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        user_group: str | core.StringOut,
        user_pool: str | core.StringOut,
    ):
        super().__init__(
            args=CognitoMemberDefinition.Args(
                client_id=client_id,
                user_group=user_group,
                user_pool=user_pool,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: str | core.StringOut = core.arg()

        user_group: str | core.StringOut = core.arg()

        user_pool: str | core.StringOut = core.arg()


@core.schema
class OidcMemberDefinition(core.Schema):

    groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        groups: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=OidcMemberDefinition.Args(
                groups=groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class MemberDefinition(core.Schema):

    cognito_member_definition: CognitoMemberDefinition | None = core.attr(
        CognitoMemberDefinition, default=None
    )

    oidc_member_definition: OidcMemberDefinition | None = core.attr(
        OidcMemberDefinition, default=None
    )

    def __init__(
        self,
        *,
        cognito_member_definition: CognitoMemberDefinition | None = None,
        oidc_member_definition: OidcMemberDefinition | None = None,
    ):
        super().__init__(
            args=MemberDefinition.Args(
                cognito_member_definition=cognito_member_definition,
                oidc_member_definition=oidc_member_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cognito_member_definition: CognitoMemberDefinition | None = core.arg(default=None)

        oidc_member_definition: OidcMemberDefinition | None = core.arg(default=None)


@core.resource(type="aws_sagemaker_workteam", namespace="aws_sagemaker")
class Workteam(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    member_definition: list[MemberDefinition] | core.ArrayOut[MemberDefinition] = core.attr(
        MemberDefinition, kind=core.Kind.array
    )

    notification_configuration: NotificationConfiguration | None = core.attr(
        NotificationConfiguration, default=None
    )

    subdomain: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    workforce_name: str | core.StringOut = core.attr(str)

    workteam_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut,
        member_definition: list[MemberDefinition] | core.ArrayOut[MemberDefinition],
        workforce_name: str | core.StringOut,
        workteam_name: str | core.StringOut,
        notification_configuration: NotificationConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workteam.Args(
                description=description,
                member_definition=member_definition,
                workforce_name=workforce_name,
                workteam_name=workteam_name,
                notification_configuration=notification_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut = core.arg()

        member_definition: list[MemberDefinition] | core.ArrayOut[MemberDefinition] = core.arg()

        notification_configuration: NotificationConfiguration | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        workforce_name: str | core.StringOut = core.arg()

        workteam_name: str | core.StringOut = core.arg()
