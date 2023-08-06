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


@core.data(type="aws_kendra_experience", namespace="aws_kendra")
class DsExperience(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    configuration: list[Configuration] | core.ArrayOut[Configuration] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    created_at: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    error_message: str | core.StringOut = core.attr(str, computed=True)

    experience_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

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
