import terrascript.core as core


@core.schema
class Endpoints(core.Schema):

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint: str | core.StringOut,
        endpoint_type: str | core.StringOut,
    ):
        super().__init__(
            args=Endpoints.Args(
                endpoint=endpoint,
                endpoint_type=endpoint_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: str | core.StringOut = core.arg()

        endpoint_type: str | core.StringOut = core.arg()


@core.schema
class ContentSourceConfiguration(core.Schema):

    data_source_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    direct_put_content: bool | core.BoolOut = core.attr(bool, computed=True)

    faq_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        data_source_ids: list[str] | core.ArrayOut[core.StringOut],
        direct_put_content: bool | core.BoolOut,
        faq_ids: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=ContentSourceConfiguration.Args(
                data_source_ids=data_source_ids,
                direct_put_content=direct_put_content,
                faq_ids=faq_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_source_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        direct_put_content: bool | core.BoolOut = core.arg()

        faq_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class UserIdentityConfiguration(core.Schema):

    identity_attribute_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        identity_attribute_name: str | core.StringOut,
    ):
        super().__init__(
            args=UserIdentityConfiguration.Args(
                identity_attribute_name=identity_attribute_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identity_attribute_name: str | core.StringOut = core.arg()


@core.schema
class Configuration(core.Schema):

    content_source_configuration: list[ContentSourceConfiguration] | core.ArrayOut[
        ContentSourceConfiguration
    ] = core.attr(ContentSourceConfiguration, computed=True, kind=core.Kind.array)

    user_identity_configuration: list[UserIdentityConfiguration] | core.ArrayOut[
        UserIdentityConfiguration
    ] = core.attr(UserIdentityConfiguration, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        content_source_configuration: list[ContentSourceConfiguration]
        | core.ArrayOut[ContentSourceConfiguration],
        user_identity_configuration: list[UserIdentityConfiguration]
        | core.ArrayOut[UserIdentityConfiguration],
    ):
        super().__init__(
            args=Configuration.Args(
                content_source_configuration=content_source_configuration,
                user_identity_configuration=user_identity_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_source_configuration: list[ContentSourceConfiguration] | core.ArrayOut[
            ContentSourceConfiguration
        ] = core.arg()

        user_identity_configuration: list[UserIdentityConfiguration] | core.ArrayOut[
            UserIdentityConfiguration
        ] = core.arg()


@core.data(type="aws_kendra_experience", namespace="kendra")
class DsExperience(core.Data):
    """
    The Amazon Resource Name (ARN) of the Experience.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A block that specifies the configuration information for your Amazon Kendra Experience. This include
    s `content_source_configuration`, which specifies the data source IDs and/or FAQ IDs, and `user_iden
    tity_configuration`, which specifies the user or group information to grant access to your Amazon Ke
    ndra Experience. Documented below.
    """
    configuration: list[Configuration] | core.ArrayOut[Configuration] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    """
    The Unix datetime that the Experience was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the Experience.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Shows the endpoint URLs for your Amazon Kendra Experiences. The URLs are unique and fully hosted by
    AWS. Documented below.
    """
    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    """
    The reason your Amazon Kendra Experience could not properly process.
    """
    error_message: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the Experience.
    """
    experience_id: str | core.StringOut = core.attr(str)

    """
    The unique identifiers of the Experience and index separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier of the index that contains the Experience.
    """
    index_id: str | core.StringOut = core.attr(str)

    """
    The name of the Experience.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Shows the Amazon Resource Name (ARN) of a role with permission to access `Query` API, `QuerySuggesti
    ons` API, `SubmitFeedback` API, and AWS SSO that stores your user and group information.
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The current processing status of your Amazon Kendra Experience. When the status is `ACTIVE`, your Am
    azon Kendra Experience is ready to use. When the status is `FAILED`, the `error_message` field conta
    ins the reason that this failed.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time that the Experience was last updated.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        experience_id: str | core.StringOut,
        index_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsExperience.Args(
                experience_id=experience_id,
                index_id=index_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        experience_id: str | core.StringOut = core.arg()

        index_id: str | core.StringOut = core.arg()
