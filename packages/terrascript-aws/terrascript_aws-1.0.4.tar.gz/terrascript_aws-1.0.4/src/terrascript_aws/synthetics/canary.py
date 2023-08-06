import terrascript.core as core


@core.schema
class RunConfig(core.Schema):

    active_tracing: bool | core.BoolOut | None = core.attr(bool, default=None)

    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    memory_in_mb: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        active_tracing: bool | core.BoolOut | None = None,
        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        memory_in_mb: int | core.IntOut | None = None,
        timeout_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=RunConfig.Args(
                active_tracing=active_tracing,
                environment_variables=environment_variables,
                memory_in_mb=memory_in_mb,
                timeout_in_seconds=timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_tracing: bool | core.BoolOut | None = core.arg(default=None)

        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        memory_in_mb: int | core.IntOut | None = core.arg(default=None)

        timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Timeline(core.Schema):

    created: str | core.StringOut = core.attr(str, computed=True)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    last_started: str | core.StringOut = core.attr(str, computed=True)

    last_stopped: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        created: str | core.StringOut,
        last_modified: str | core.StringOut,
        last_started: str | core.StringOut,
        last_stopped: str | core.StringOut,
    ):
        super().__init__(
            args=Timeline.Args(
                created=created,
                last_modified=last_modified,
                last_started=last_started,
                last_stopped=last_stopped,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        created: str | core.StringOut = core.arg()

        last_modified: str | core.StringOut = core.arg()

        last_started: str | core.StringOut = core.arg()

        last_stopped: str | core.StringOut = core.arg()


@core.schema
class Schedule(core.Schema):

    duration_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    expression: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        expression: str | core.StringOut,
        duration_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Schedule.Args(
                expression=expression,
                duration_in_seconds=duration_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration_in_seconds: int | core.IntOut | None = core.arg(default=None)

        expression: str | core.StringOut = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        vpc_id: str | core.StringOut,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                vpc_id=vpc_id,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()


@core.schema
class S3Encryption(core.Schema):

    encryption_mode: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_mode: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Encryption.Args(
                encryption_mode=encryption_mode,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_mode: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ArtifactConfig(core.Schema):

    s3_encryption: S3Encryption | None = core.attr(S3Encryption, default=None)

    def __init__(
        self,
        *,
        s3_encryption: S3Encryption | None = None,
    ):
        super().__init__(
            args=ArtifactConfig.Args(
                s3_encryption=s3_encryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_encryption: S3Encryption | None = core.arg(default=None)


@core.resource(type="aws_synthetics_canary", namespace="synthetics")
class Canary(core.Resource):
    """
    Amazon Resource Name (ARN) of the Canary.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) configuration for canary artifacts, including the encryption-at-rest settings for artifac
    ts that the canary uploads to Amazon S3. See [Artifact Config](#artifact_config).
    """
    artifact_config: ArtifactConfig | None = core.attr(ArtifactConfig, default=None)

    """
    (Required) Location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary
    .
    """
    artifact_s3_location: str | core.StringOut = core.attr(str)

    """
    (Optional)  Specifies whether to also delete the Lambda functions and layers used by this canary. Th
    e default is `false`.
    """
    delete_lambda: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    ARN of the Lambda function that is used as your canary's engine.
    """
    engine_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of the IAM role to be used to run the canary. see [AWS Docs](https://docs.aws.amazon.
    com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html#API_CreateCanary_RequestSyntax) for p
    ermissions needs for IAM Role.
    """
    execution_role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Number of days to retain data about failed runs of this canary. If you omit this field, t
    he default of 31 days is used. The valid range is 1 to 455 days.
    """
    failure_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) Entry point to use for the source code when running the canary. This value must end with
    the string `.handler` .
    """
    handler: str | core.StringOut = core.attr(str)

    """
    Name for this canary.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name for this canary. Has a maximum length of 21 characters. Valid characters are lowerca
    se alphanumeric, hyphen, or underscore.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for individual canary runs. Detailed below.
    """
    run_config: RunConfig | None = core.attr(RunConfig, default=None, computed=True)

    """
    (Required) Runtime version to use for the canary. Versions change often so consult the [Amazon Cloud
    Watch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synth
    etics_Canaries_Library.html) for the latest valid versions. Values include `syn-python-selenium-1.0`
    , `syn-nodejs-puppeteer-3.0`, `syn-nodejs-2.2`, `syn-nodejs-2.1`, `syn-nodejs-2.0`, and `syn-1.0`.
    """
    runtime_version: str | core.StringOut = core.attr(str)

    """
    (Optional) Full bucket name which is used if your canary script is located in S3. The bucket must al
    ready exist. Specify the full bucket name including s3:// as the start of the bucket name. **Conflic
    ts with `zip_file`.**
    """
    s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 key of your script. **Conflicts with `zip_file`.**
    """
    s3_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 version ID of your script. **Conflicts with `zip_file`.**
    """
    s3_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Configuration block providing how often the canary is to run and when these test runs ar
    e to stop. Detailed below.
    """
    schedule: Schedule = core.attr(Schedule)

    """
    ARN of the Lambda layer where Synthetics stores the canary script code.
    """
    source_location_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to run or stop the canary.
    """
    start_canary: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Canary status.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Number of days to retain data about successful runs of this canary. If you omit this fiel
    d, the default of 31 days is used. The valid range is 1 to 455 days.
    """
    success_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    Structure that contains information about when the canary was created, modified, and most recently r
    un. see [Timeline](#timeline).
    """
    timeline: list[Timeline] | core.ArrayOut[Timeline] = core.attr(
        Timeline, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block. Detailed below.
    """
    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    """
    (Optional) ZIP file that contains the script, if you input your canary script directly into the cana
    ry instead of referring to an S3 location. It can be up to 5 MB. **Conflicts with `s3_bucket`, `s3_k
    ey`, and `s3_version`.**
    """
    zip_file: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        artifact_s3_location: str | core.StringOut,
        execution_role_arn: str | core.StringOut,
        handler: str | core.StringOut,
        name: str | core.StringOut,
        runtime_version: str | core.StringOut,
        schedule: Schedule,
        artifact_config: ArtifactConfig | None = None,
        delete_lambda: bool | core.BoolOut | None = None,
        failure_retention_period: int | core.IntOut | None = None,
        run_config: RunConfig | None = None,
        s3_bucket: str | core.StringOut | None = None,
        s3_key: str | core.StringOut | None = None,
        s3_version: str | core.StringOut | None = None,
        start_canary: bool | core.BoolOut | None = None,
        success_retention_period: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_config: VpcConfig | None = None,
        zip_file: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Canary.Args(
                artifact_s3_location=artifact_s3_location,
                execution_role_arn=execution_role_arn,
                handler=handler,
                name=name,
                runtime_version=runtime_version,
                schedule=schedule,
                artifact_config=artifact_config,
                delete_lambda=delete_lambda,
                failure_retention_period=failure_retention_period,
                run_config=run_config,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_version=s3_version,
                start_canary=start_canary,
                success_retention_period=success_retention_period,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                zip_file=zip_file,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifact_config: ArtifactConfig | None = core.arg(default=None)

        artifact_s3_location: str | core.StringOut = core.arg()

        delete_lambda: bool | core.BoolOut | None = core.arg(default=None)

        execution_role_arn: str | core.StringOut = core.arg()

        failure_retention_period: int | core.IntOut | None = core.arg(default=None)

        handler: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        run_config: RunConfig | None = core.arg(default=None)

        runtime_version: str | core.StringOut = core.arg()

        s3_bucket: str | core.StringOut | None = core.arg(default=None)

        s3_key: str | core.StringOut | None = core.arg(default=None)

        s3_version: str | core.StringOut | None = core.arg(default=None)

        schedule: Schedule = core.arg()

        start_canary: bool | core.BoolOut | None = core.arg(default=None)

        success_retention_period: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)

        zip_file: str | core.StringOut | None = core.arg(default=None)
