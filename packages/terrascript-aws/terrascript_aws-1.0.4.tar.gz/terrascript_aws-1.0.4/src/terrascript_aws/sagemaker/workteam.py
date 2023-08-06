import terrascript.core as core


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


@core.resource(type="aws_sagemaker_workteam", namespace="sagemaker")
class Workteam(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Workteam.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A description of the work team.
    """
    description: str | core.StringOut = core.attr(str)

    """
    The name of the Workteam.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of Member Definitions that contains objects that identify the workers that make up
    the work team. Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (I
    dP). For private workforces created using Amazon Cognito use `cognito_member_definition`. For workfo
    rces created using your own OIDC identity provider (IdP) use `oidc_member_definition`. Do not provid
    e input for both of these parameters in a single request. see [Member Definition](#member-definition
    ) details below.
    """
    member_definition: list[MemberDefinition] | core.ArrayOut[MemberDefinition] = core.attr(
        MemberDefinition, kind=core.Kind.array
    )

    """
    (Optional) Configures notification of workers regarding available or expiring work items. see [Notif
    ication Configuration](#notification-configuration) details below.
    """
    notification_configuration: NotificationConfiguration | None = core.attr(
        NotificationConfiguration, default=None
    )

    """
    The subdomain for your OIDC Identity Provider.
    """
    subdomain: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The name of the Workteam (must be unique).
    """
    workforce_name: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the workforce.
    """
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
