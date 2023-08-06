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


@core.resource(type="aws_appconfig_configuration_profile", namespace="aws_appconfig")
class ConfigurationProfile(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    configuration_profile_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    location_uri: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    retrieval_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

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
