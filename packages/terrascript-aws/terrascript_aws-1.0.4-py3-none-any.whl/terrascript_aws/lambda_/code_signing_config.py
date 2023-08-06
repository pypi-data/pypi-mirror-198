import terrascript.core as core


@core.schema
class Policies(core.Schema):

    untrusted_artifact_on_deployment: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        untrusted_artifact_on_deployment: str | core.StringOut,
    ):
        super().__init__(
            args=Policies.Args(
                untrusted_artifact_on_deployment=untrusted_artifact_on_deployment,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        untrusted_artifact_on_deployment: str | core.StringOut = core.arg()


@core.schema
class AllowedPublishers(core.Schema):

    signing_profile_version_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        signing_profile_version_arns: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=AllowedPublishers.Args(
                signing_profile_version_arns=signing_profile_version_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        signing_profile_version_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_lambda_code_signing_config", namespace="lambda_")
class CodeSigningConfig(core.Resource):

    allowed_publishers: AllowedPublishers = core.attr(AllowedPublishers)

    """
    The Amazon Resource Name (ARN) of the code signing configuration.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Unique identifier for the code signing configuration.
    """
    config_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Descriptive name for this code signing configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time that the code signing configuration was last modified.
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    policies: Policies | None = core.attr(Policies, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        allowed_publishers: AllowedPublishers,
        description: str | core.StringOut | None = None,
        policies: Policies | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CodeSigningConfig.Args(
                allowed_publishers=allowed_publishers,
                description=description,
                policies=policies,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_publishers: AllowedPublishers = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        policies: Policies | None = core.arg(default=None)
