import terrascript.core as core


@core.schema
class AllowedPublishers(core.Schema):

    signing_profile_version_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
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


@core.schema
class Policies(core.Schema):

    untrusted_artifact_on_deployment: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_lambda_code_signing_config", namespace="aws_lambda_")
class DsCodeSigningConfig(core.Data):

    allowed_publishers: list[AllowedPublishers] | core.ArrayOut[AllowedPublishers] = core.attr(
        AllowedPublishers, computed=True, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str)

    config_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    policies: list[Policies] | core.ArrayOut[Policies] = core.attr(
        Policies, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsCodeSigningConfig.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()
