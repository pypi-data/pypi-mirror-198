import terrascript.core as core


@core.schema
class SecondaryArtifacts(core.Schema):

    artifact_identifier: str | core.StringOut = core.attr(str)

    bucket_owner_access: str | core.StringOut | None = core.attr(str, default=None)

    encryption_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    namespace_type: str | core.StringOut | None = core.attr(str, default=None)

    override_artifact_name: bool | core.BoolOut | None = core.attr(bool, default=None)

    packaging: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        artifact_identifier: str | core.StringOut,
        type: str | core.StringOut,
        bucket_owner_access: str | core.StringOut | None = None,
        encryption_disabled: bool | core.BoolOut | None = None,
        location: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        namespace_type: str | core.StringOut | None = None,
        override_artifact_name: bool | core.BoolOut | None = None,
        packaging: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SecondaryArtifacts.Args(
                artifact_identifier=artifact_identifier,
                type=type,
                bucket_owner_access=bucket_owner_access,
                encryption_disabled=encryption_disabled,
                location=location,
                name=name,
                namespace_type=namespace_type,
                override_artifact_name=override_artifact_name,
                packaging=packaging,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        artifact_identifier: str | core.StringOut = core.arg()

        bucket_owner_access: str | core.StringOut | None = core.arg(default=None)

        encryption_disabled: bool | core.BoolOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        namespace_type: str | core.StringOut | None = core.arg(default=None)

        override_artifact_name: bool | core.BoolOut | None = core.arg(default=None)

        packaging: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class CloudwatchLogs(core.Schema):

    group_name: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut | None = core.attr(str, default=None)

    stream_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        group_name: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        stream_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                group_name=group_name,
                status=status,
                stream_name=stream_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_name: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        stream_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3Logs(core.Schema):

    bucket_owner_access: str | core.StringOut | None = core.attr(str, default=None)

    encryption_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_owner_access: str | core.StringOut | None = None,
        encryption_disabled: bool | core.BoolOut | None = None,
        location: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Logs.Args(
                bucket_owner_access=bucket_owner_access,
                encryption_disabled=encryption_disabled,
                location=location,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_owner_access: str | core.StringOut | None = core.arg(default=None)

        encryption_disabled: bool | core.BoolOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LogsConfig(core.Schema):

    cloudwatch_logs: CloudwatchLogs | None = core.attr(CloudwatchLogs, default=None)

    s3_logs: S3Logs | None = core.attr(S3Logs, default=None)

    def __init__(
        self,
        *,
        cloudwatch_logs: CloudwatchLogs | None = None,
        s3_logs: S3Logs | None = None,
    ):
        super().__init__(
            args=LogsConfig.Args(
                cloudwatch_logs=cloudwatch_logs,
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs: CloudwatchLogs | None = core.arg(default=None)

        s3_logs: S3Logs | None = core.arg(default=None)


@core.schema
class GitSubmodulesConfig(core.Schema):

    fetch_submodules: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        fetch_submodules: bool | core.BoolOut,
    ):
        super().__init__(
            args=GitSubmodulesConfig.Args(
                fetch_submodules=fetch_submodules,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fetch_submodules: bool | core.BoolOut = core.arg()


@core.schema
class BuildStatusConfig(core.Schema):

    context: str | core.StringOut | None = core.attr(str, default=None)

    target_url: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        context: str | core.StringOut | None = None,
        target_url: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=BuildStatusConfig.Args(
                context=context,
                target_url=target_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        context: str | core.StringOut | None = core.arg(default=None)

        target_url: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Auth(core.Schema):

    resource: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        resource: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Auth.Args(
                type=type,
                resource=resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class Source(core.Schema):

    auth: Auth | None = core.attr(Auth, default=None)

    build_status_config: BuildStatusConfig | None = core.attr(BuildStatusConfig, default=None)

    buildspec: str | core.StringOut | None = core.attr(str, default=None)

    git_clone_depth: int | core.IntOut | None = core.attr(int, default=None)

    git_submodules_config: GitSubmodulesConfig | None = core.attr(GitSubmodulesConfig, default=None)

    insecure_ssl: bool | core.BoolOut | None = core.attr(bool, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    report_build_status: bool | core.BoolOut | None = core.attr(bool, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        auth: Auth | None = None,
        build_status_config: BuildStatusConfig | None = None,
        buildspec: str | core.StringOut | None = None,
        git_clone_depth: int | core.IntOut | None = None,
        git_submodules_config: GitSubmodulesConfig | None = None,
        insecure_ssl: bool | core.BoolOut | None = None,
        location: str | core.StringOut | None = None,
        report_build_status: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Source.Args(
                type=type,
                auth=auth,
                build_status_config=build_status_config,
                buildspec=buildspec,
                git_clone_depth=git_clone_depth,
                git_submodules_config=git_submodules_config,
                insecure_ssl=insecure_ssl,
                location=location,
                report_build_status=report_build_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth: Auth | None = core.arg(default=None)

        build_status_config: BuildStatusConfig | None = core.arg(default=None)

        buildspec: str | core.StringOut | None = core.arg(default=None)

        git_clone_depth: int | core.IntOut | None = core.arg(default=None)

        git_submodules_config: GitSubmodulesConfig | None = core.arg(default=None)

        insecure_ssl: bool | core.BoolOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        report_build_status: bool | core.BoolOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class Restrictions(core.Schema):

    compute_types_allowed: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    maximum_builds_allowed: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        compute_types_allowed: list[str] | core.ArrayOut[core.StringOut] | None = None,
        maximum_builds_allowed: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Restrictions.Args(
                compute_types_allowed=compute_types_allowed,
                maximum_builds_allowed=maximum_builds_allowed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_types_allowed: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        maximum_builds_allowed: int | core.IntOut | None = core.arg(default=None)


@core.schema
class BuildBatchConfig(core.Schema):

    combine_artifacts: bool | core.BoolOut | None = core.attr(bool, default=None)

    restrictions: Restrictions | None = core.attr(Restrictions, default=None)

    service_role: str | core.StringOut = core.attr(str)

    timeout_in_mins: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        service_role: str | core.StringOut,
        combine_artifacts: bool | core.BoolOut | None = None,
        restrictions: Restrictions | None = None,
        timeout_in_mins: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=BuildBatchConfig.Args(
                service_role=service_role,
                combine_artifacts=combine_artifacts,
                restrictions=restrictions,
                timeout_in_mins=timeout_in_mins,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        combine_artifacts: bool | core.BoolOut | None = core.arg(default=None)

        restrictions: Restrictions | None = core.arg(default=None)

        service_role: str | core.StringOut = core.arg()

        timeout_in_mins: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Artifacts(core.Schema):

    artifact_identifier: str | core.StringOut | None = core.attr(str, default=None)

    bucket_owner_access: str | core.StringOut | None = core.attr(str, default=None)

    encryption_disabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    namespace_type: str | core.StringOut | None = core.attr(str, default=None)

    override_artifact_name: bool | core.BoolOut | None = core.attr(bool, default=None)

    packaging: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        artifact_identifier: str | core.StringOut | None = None,
        bucket_owner_access: str | core.StringOut | None = None,
        encryption_disabled: bool | core.BoolOut | None = None,
        location: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        namespace_type: str | core.StringOut | None = None,
        override_artifact_name: bool | core.BoolOut | None = None,
        packaging: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Artifacts.Args(
                type=type,
                artifact_identifier=artifact_identifier,
                bucket_owner_access=bucket_owner_access,
                encryption_disabled=encryption_disabled,
                location=location,
                name=name,
                namespace_type=namespace_type,
                override_artifact_name=override_artifact_name,
                packaging=packaging,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        artifact_identifier: str | core.StringOut | None = core.arg(default=None)

        bucket_owner_access: str | core.StringOut | None = core.arg(default=None)

        encryption_disabled: bool | core.BoolOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        namespace_type: str | core.StringOut | None = core.arg(default=None)

        override_artifact_name: bool | core.BoolOut | None = core.arg(default=None)

        packaging: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class SecondarySources(core.Schema):

    auth: Auth | None = core.attr(Auth, default=None)

    build_status_config: BuildStatusConfig | None = core.attr(BuildStatusConfig, default=None)

    buildspec: str | core.StringOut | None = core.attr(str, default=None)

    git_clone_depth: int | core.IntOut | None = core.attr(int, default=None)

    git_submodules_config: GitSubmodulesConfig | None = core.attr(GitSubmodulesConfig, default=None)

    insecure_ssl: bool | core.BoolOut | None = core.attr(bool, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    report_build_status: bool | core.BoolOut | None = core.attr(bool, default=None)

    source_identifier: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source_identifier: str | core.StringOut,
        type: str | core.StringOut,
        auth: Auth | None = None,
        build_status_config: BuildStatusConfig | None = None,
        buildspec: str | core.StringOut | None = None,
        git_clone_depth: int | core.IntOut | None = None,
        git_submodules_config: GitSubmodulesConfig | None = None,
        insecure_ssl: bool | core.BoolOut | None = None,
        location: str | core.StringOut | None = None,
        report_build_status: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=SecondarySources.Args(
                source_identifier=source_identifier,
                type=type,
                auth=auth,
                build_status_config=build_status_config,
                buildspec=buildspec,
                git_clone_depth=git_clone_depth,
                git_submodules_config=git_submodules_config,
                insecure_ssl=insecure_ssl,
                location=location,
                report_build_status=report_build_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth: Auth | None = core.arg(default=None)

        build_status_config: BuildStatusConfig | None = core.arg(default=None)

        buildspec: str | core.StringOut | None = core.arg(default=None)

        git_clone_depth: int | core.IntOut | None = core.arg(default=None)

        git_submodules_config: GitSubmodulesConfig | None = core.arg(default=None)

        insecure_ssl: bool | core.BoolOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        report_build_status: bool | core.BoolOut | None = core.arg(default=None)

        source_identifier: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class RegistryCredential(core.Schema):

    credential: str | core.StringOut = core.attr(str)

    credential_provider: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        credential: str | core.StringOut,
        credential_provider: str | core.StringOut,
    ):
        super().__init__(
            args=RegistryCredential.Args(
                credential=credential,
                credential_provider=credential_provider,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credential: str | core.StringOut = core.arg()

        credential_provider: str | core.StringOut = core.arg()


@core.schema
class EnvironmentVariable(core.Schema):

    name: str | core.StringOut = core.attr(str)

    type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EnvironmentVariable.Args(
                name=name,
                value=value,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.schema
class Environment(core.Schema):

    certificate: str | core.StringOut | None = core.attr(str, default=None)

    compute_type: str | core.StringOut = core.attr(str)

    environment_variable: list[EnvironmentVariable] | core.ArrayOut[
        EnvironmentVariable
    ] | None = core.attr(EnvironmentVariable, default=None, kind=core.Kind.array)

    image: str | core.StringOut = core.attr(str)

    image_pull_credentials_type: str | core.StringOut | None = core.attr(str, default=None)

    privileged_mode: bool | core.BoolOut | None = core.attr(bool, default=None)

    registry_credential: RegistryCredential | None = core.attr(RegistryCredential, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        compute_type: str | core.StringOut,
        image: str | core.StringOut,
        type: str | core.StringOut,
        certificate: str | core.StringOut | None = None,
        environment_variable: list[EnvironmentVariable]
        | core.ArrayOut[EnvironmentVariable]
        | None = None,
        image_pull_credentials_type: str | core.StringOut | None = None,
        privileged_mode: bool | core.BoolOut | None = None,
        registry_credential: RegistryCredential | None = None,
    ):
        super().__init__(
            args=Environment.Args(
                compute_type=compute_type,
                image=image,
                type=type,
                certificate=certificate,
                environment_variable=environment_variable,
                image_pull_credentials_type=image_pull_credentials_type,
                privileged_mode=privileged_mode,
                registry_credential=registry_credential,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: str | core.StringOut | None = core.arg(default=None)

        compute_type: str | core.StringOut = core.arg()

        environment_variable: list[EnvironmentVariable] | core.ArrayOut[
            EnvironmentVariable
        ] | None = core.arg(default=None)

        image: str | core.StringOut = core.arg()

        image_pull_credentials_type: str | core.StringOut | None = core.arg(default=None)

        privileged_mode: bool | core.BoolOut | None = core.arg(default=None)

        registry_credential: RegistryCredential | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class SecondarySourceVersion(core.Schema):

    source_identifier: str | core.StringOut = core.attr(str)

    source_version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source_identifier: str | core.StringOut,
        source_version: str | core.StringOut,
    ):
        super().__init__(
            args=SecondarySourceVersion.Args(
                source_identifier=source_identifier,
                source_version=source_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source_identifier: str | core.StringOut = core.arg()

        source_version: str | core.StringOut = core.arg()


@core.schema
class Cache(core.Schema):

    location: str | core.StringOut | None = core.attr(str, default=None)

    modes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        location: str | core.StringOut | None = None,
        modes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Cache.Args(
                location=location,
                modes=modes,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        location: str | core.StringOut | None = core.arg(default=None)

        modes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnets: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnets=subnets,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class FileSystemLocations(core.Schema):

    identifier: str | core.StringOut | None = core.attr(str, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    mount_options: str | core.StringOut | None = core.attr(str, default=None)

    mount_point: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        identifier: str | core.StringOut | None = None,
        location: str | core.StringOut | None = None,
        mount_options: str | core.StringOut | None = None,
        mount_point: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FileSystemLocations.Args(
                identifier=identifier,
                location=location,
                mount_options=mount_options,
                mount_point=mount_point,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifier: str | core.StringOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        mount_options: str | core.StringOut | None = core.arg(default=None)

        mount_point: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_codebuild_project", namespace="codebuild")
class Project(core.Resource):
    """
    ARN of the CodeBuild project.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block. Detailed below.
    """
    artifacts: Artifacts = core.attr(Artifacts)

    """
    (Optional) Generates a publicly-accessible URL for the projects build badge. Available as `badge_url
    attribute when enabled.
    """
    badge_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    URL of the build badge when `badge_enabled` is enabled.
    """
    badge_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Defines the batch build options for the project.
    """
    build_batch_config: BuildBatchConfig | None = core.attr(BuildBatchConfig, default=None)

    """
    (Optional) Number of minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out an
    y related build that does not get marked as completed. The default is 60 minutes.
    """
    build_timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Configuration block. Detailed below.
    """
    cache: Cache | None = core.attr(Cache, default=None)

    """
    (Optional) Specify a maximum number of concurrent builds for the project. The value specified must b
    e greater than 0 and less than the account concurrent running builds limit.
    """
    concurrent_build_limit: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Short description of the project.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting
    the build project's build output artifacts.
    """
    encryption_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Configuration block. Detailed below.
    """
    environment: Environment = core.attr(Environment)

    """
    (Optional) A set of file system locations to to mount inside the build. File system locations are do
    cumented below.
    """
    file_system_locations: list[FileSystemLocations] | core.ArrayOut[
        FileSystemLocations
    ] | None = core.attr(FileSystemLocations, default=None, kind=core.Kind.array)

    """
    Name (if imported via `name`) or ARN (if created via Terraform or imported via ARN) of the CodeBuild
    project.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block. Detailed below.
    """
    logs_config: LogsConfig | None = core.attr(LogsConfig, default=None)

    """
    (Required) Project's name.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the visibility of the project's builds. Possible values are: `PUBLIC_READ` and
    PRIVATE`. Default value is `PRIVATE`.
    """
    project_visibility: str | core.StringOut | None = core.attr(str, default=None)

    """
    The project identifier used with the public build APIs.
    """
    public_project_alias: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Number of minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it tim
    es out. The default is 8 hours.
    """
    queued_timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts
    for the project's builds.
    """
    resource_access_role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Configuration block. Detailed below.
    """
    secondary_artifacts: list[SecondaryArtifacts] | core.ArrayOut[
        SecondaryArtifacts
    ] | None = core.attr(SecondaryArtifacts, default=None, kind=core.Kind.array)

    """
    (Optional) Configuration block. Detailed below.
    """
    secondary_source_version: list[SecondarySourceVersion] | core.ArrayOut[
        SecondarySourceVersion
    ] | None = core.attr(SecondarySourceVersion, default=None, kind=core.Kind.array)

    """
    (Optional) Configuration block. Detailed below.
    """
    secondary_sources: list[SecondarySources] | core.ArrayOut[SecondarySources] | None = core.attr(
        SecondarySources, default=None, kind=core.Kind.array
    )

    """
    (Required) Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enab
    les AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
    """
    service_role: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block. Detailed below.
    """
    source: Source = core.attr(Source)

    """
    (Optional) Version of the build input to be built for this project. If not specified, the latest ver
    sion is used.
    """
    source_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
    (Optional) Configuration block. Detailed below.
    """
    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        artifacts: Artifacts,
        environment: Environment,
        name: str | core.StringOut,
        service_role: str | core.StringOut,
        source: Source,
        badge_enabled: bool | core.BoolOut | None = None,
        build_batch_config: BuildBatchConfig | None = None,
        build_timeout: int | core.IntOut | None = None,
        cache: Cache | None = None,
        concurrent_build_limit: int | core.IntOut | None = None,
        description: str | core.StringOut | None = None,
        encryption_key: str | core.StringOut | None = None,
        file_system_locations: list[FileSystemLocations]
        | core.ArrayOut[FileSystemLocations]
        | None = None,
        logs_config: LogsConfig | None = None,
        project_visibility: str | core.StringOut | None = None,
        queued_timeout: int | core.IntOut | None = None,
        resource_access_role: str | core.StringOut | None = None,
        secondary_artifacts: list[SecondaryArtifacts]
        | core.ArrayOut[SecondaryArtifacts]
        | None = None,
        secondary_source_version: list[SecondarySourceVersion]
        | core.ArrayOut[SecondarySourceVersion]
        | None = None,
        secondary_sources: list[SecondarySources] | core.ArrayOut[SecondarySources] | None = None,
        source_version: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_config: VpcConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Project.Args(
                artifacts=artifacts,
                environment=environment,
                name=name,
                service_role=service_role,
                source=source,
                badge_enabled=badge_enabled,
                build_batch_config=build_batch_config,
                build_timeout=build_timeout,
                cache=cache,
                concurrent_build_limit=concurrent_build_limit,
                description=description,
                encryption_key=encryption_key,
                file_system_locations=file_system_locations,
                logs_config=logs_config,
                project_visibility=project_visibility,
                queued_timeout=queued_timeout,
                resource_access_role=resource_access_role,
                secondary_artifacts=secondary_artifacts,
                secondary_source_version=secondary_source_version,
                secondary_sources=secondary_sources,
                source_version=source_version,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifacts: Artifacts = core.arg()

        badge_enabled: bool | core.BoolOut | None = core.arg(default=None)

        build_batch_config: BuildBatchConfig | None = core.arg(default=None)

        build_timeout: int | core.IntOut | None = core.arg(default=None)

        cache: Cache | None = core.arg(default=None)

        concurrent_build_limit: int | core.IntOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        encryption_key: str | core.StringOut | None = core.arg(default=None)

        environment: Environment = core.arg()

        file_system_locations: list[FileSystemLocations] | core.ArrayOut[
            FileSystemLocations
        ] | None = core.arg(default=None)

        logs_config: LogsConfig | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        project_visibility: str | core.StringOut | None = core.arg(default=None)

        queued_timeout: int | core.IntOut | None = core.arg(default=None)

        resource_access_role: str | core.StringOut | None = core.arg(default=None)

        secondary_artifacts: list[SecondaryArtifacts] | core.ArrayOut[
            SecondaryArtifacts
        ] | None = core.arg(default=None)

        secondary_source_version: list[SecondarySourceVersion] | core.ArrayOut[
            SecondarySourceVersion
        ] | None = core.arg(default=None)

        secondary_sources: list[SecondarySources] | core.ArrayOut[
            SecondarySources
        ] | None = core.arg(default=None)

        service_role: str | core.StringOut = core.arg()

        source: Source = core.arg()

        source_version: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)
