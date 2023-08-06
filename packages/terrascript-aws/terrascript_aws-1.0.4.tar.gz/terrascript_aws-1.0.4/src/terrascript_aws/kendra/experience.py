import terrascript.core as core


@core.schema
class UserIdentityConfiguration(core.Schema):

    identity_attribute_name: str | core.StringOut = core.attr(str)

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
class ContentSourceConfiguration(core.Schema):

    data_source_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    direct_put_content: bool | core.BoolOut | None = core.attr(bool, default=None)

    faq_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        data_source_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        direct_put_content: bool | core.BoolOut | None = None,
        faq_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
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
        data_source_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        direct_put_content: bool | core.BoolOut | None = core.arg(default=None)

        faq_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    content_source_configuration: ContentSourceConfiguration | None = core.attr(
        ContentSourceConfiguration, default=None, computed=True
    )

    user_identity_configuration: UserIdentityConfiguration | None = core.attr(
        UserIdentityConfiguration, default=None
    )

    def __init__(
        self,
        *,
        content_source_configuration: ContentSourceConfiguration | None = None,
        user_identity_configuration: UserIdentityConfiguration | None = None,
    ):
        super().__init__(
            args=Configuration.Args(
                content_source_configuration=content_source_configuration,
                user_identity_configuration=user_identity_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_source_configuration: ContentSourceConfiguration | None = core.arg(default=None)

        user_identity_configuration: UserIdentityConfiguration | None = core.arg(default=None)


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


@core.resource(type="aws_kendra_experience", namespace="kendra")
class Experience(core.Resource):
    """
    ARN of the Experience.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration information for your Amazon Kendra experience. Terraform will only perform
    drift detection of its value when present in a configuration. [Detailed below](#configuration).
    """
    configuration: Configuration | None = core.attr(Configuration, default=None, computed=True)

    """
    (Optional, Forces new resource if removed) A description for your Amazon Kendra experience.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Shows the endpoint URLs for your Amazon Kendra experiences. The URLs are unique and fully hosted by
    AWS.
    """
    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    """
    The unique identifier of the experience.
    """
    experience_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifiers of the experience and index separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The identifier of the index for your Amazon Kendra experience.
    """
    index_id: str | core.StringOut = core.attr(str)

    """
    (Required) A name for your Amazon Kendra experience.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of a role with permission to access `Query API`, `QuerySug
    gestions API`, `SubmitFeedback API`, and `AWS SSO` that stores your user and group information. For
    more information, see [IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam
    roles.html).
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    The current processing status of your Amazon Kendra experience.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: str | core.StringOut,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        configuration: Configuration | None = None,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Experience.Args(
                index_id=index_id,
                name=name,
                role_arn=role_arn,
                configuration=configuration,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Configuration | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        index_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()
