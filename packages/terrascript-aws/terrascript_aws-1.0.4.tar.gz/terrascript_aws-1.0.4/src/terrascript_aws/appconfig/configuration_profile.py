import terrascript.core as core


@core.schema
class Validator(core.Schema):

    content: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        content: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Validator.Args(
                type=type,
                content=content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_appconfig_configuration_profile", namespace="appconfig")
class ConfigurationProfile(core.Resource):
    """
    (Required, Forces new resource) The application ID. Must be between 4 and 7 characters in length.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the AppConfig Configuration Profile.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The configuration profile ID.
    """
    configuration_profile_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the configuration profile. Can be at most 1024 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The AppConfig configuration profile ID and application ID separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) A URI to locate the configuration. You can specify the AWS AppConfig
    hosted configuration store, Systems Manager (SSM) document, an SSM Parameter Store parameter, or an
    Amazon S3 object. For the hosted configuration store, specify `hosted`. For an SSM document, specif
    y either the document name in the format `ssm-document://<Document_name>` or the Amazon Resource Nam
    e (ARN). For a parameter, specify either the parameter name in the format `ssm-parameter://<Paramete
    r_name>` or the ARN. For an Amazon S3 object, specify the URI in the following format: `s3://<bucket
    >/<objectKey>`.
    """
    location_uri: str | core.StringOut = core.attr(str)

    """
    (Required) The name for the configuration profile. Must be between 1 and 64 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The ARN of an IAM role with permission to access the configuration at the specified `loca
    tion_uri`. A retrieval role ARN is not required for configurations stored in the AWS AppConfig `host
    ed` configuration store. It is required for all other sources that store your configuration.
    """
    retrieval_role_arn: str | core.StringOut | None = core.attr(str, default=None)

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
    (Optional) The type of configurations contained in the profile. Valid values: `AWS.AppConfig.Feature
    Flags` and `AWS.Freeform`.  Default: `AWS.Freeform`.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A set of methods for validating the configuration. Maximum of 2. See [Validator](#validat
    or) below for more details.
    """
    validator: list[Validator] | core.ArrayOut[Validator] | None = core.attr(
        Validator, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        location_uri: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        retrieval_role_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        validator: list[Validator] | core.ArrayOut[Validator] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationProfile.Args(
                application_id=application_id,
                location_uri=location_uri,
                name=name,
                description=description,
                retrieval_role_arn=retrieval_role_arn,
                tags=tags,
                tags_all=tags_all,
                type=type,
                validator=validator,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        location_uri: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        retrieval_role_arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        validator: list[Validator] | core.ArrayOut[Validator] | None = core.arg(default=None)
