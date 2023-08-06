import terrascript.core as core


@core.schema
class EngineVersion(core.Schema):

    effective_engine_version: str | core.StringOut = core.attr(str, computed=True)

    selected_engine_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        effective_engine_version: str | core.StringOut,
        selected_engine_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EngineVersion.Args(
                effective_engine_version=effective_engine_version,
                selected_engine_version=selected_engine_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        effective_engine_version: str | core.StringOut = core.arg()

        selected_engine_version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AclConfiguration(core.Schema):

    s3_acl_option: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_acl_option: str | core.StringOut,
    ):
        super().__init__(
            args=AclConfiguration.Args(
                s3_acl_option=s3_acl_option,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_acl_option: str | core.StringOut = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    encryption_option: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_option: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                encryption_option=encryption_option,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_option: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResultConfiguration(core.Schema):

    acl_configuration: AclConfiguration | None = core.attr(AclConfiguration, default=None)

    encryption_configuration: EncryptionConfiguration | None = core.attr(
        EncryptionConfiguration, default=None
    )

    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    output_location: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        acl_configuration: AclConfiguration | None = None,
        encryption_configuration: EncryptionConfiguration | None = None,
        expected_bucket_owner: str | core.StringOut | None = None,
        output_location: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ResultConfiguration.Args(
                acl_configuration=acl_configuration,
                encryption_configuration=encryption_configuration,
                expected_bucket_owner=expected_bucket_owner,
                output_location=output_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl_configuration: AclConfiguration | None = core.arg(default=None)

        encryption_configuration: EncryptionConfiguration | None = core.arg(default=None)

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        output_location: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    bytes_scanned_cutoff_per_query: int | core.IntOut | None = core.attr(int, default=None)

    enforce_workgroup_configuration: bool | core.BoolOut | None = core.attr(bool, default=None)

    engine_version: EngineVersion | None = core.attr(EngineVersion, default=None)

    publish_cloudwatch_metrics_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    requester_pays_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    result_configuration: ResultConfiguration | None = core.attr(ResultConfiguration, default=None)

    def __init__(
        self,
        *,
        bytes_scanned_cutoff_per_query: int | core.IntOut | None = None,
        enforce_workgroup_configuration: bool | core.BoolOut | None = None,
        engine_version: EngineVersion | None = None,
        publish_cloudwatch_metrics_enabled: bool | core.BoolOut | None = None,
        requester_pays_enabled: bool | core.BoolOut | None = None,
        result_configuration: ResultConfiguration | None = None,
    ):
        super().__init__(
            args=Configuration.Args(
                bytes_scanned_cutoff_per_query=bytes_scanned_cutoff_per_query,
                enforce_workgroup_configuration=enforce_workgroup_configuration,
                engine_version=engine_version,
                publish_cloudwatch_metrics_enabled=publish_cloudwatch_metrics_enabled,
                requester_pays_enabled=requester_pays_enabled,
                result_configuration=result_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bytes_scanned_cutoff_per_query: int | core.IntOut | None = core.arg(default=None)

        enforce_workgroup_configuration: bool | core.BoolOut | None = core.arg(default=None)

        engine_version: EngineVersion | None = core.arg(default=None)

        publish_cloudwatch_metrics_enabled: bool | core.BoolOut | None = core.arg(default=None)

        requester_pays_enabled: bool | core.BoolOut | None = core.arg(default=None)

        result_configuration: ResultConfiguration | None = core.arg(default=None)


@core.resource(type="aws_athena_workgroup", namespace="athena")
class Workgroup(core.Resource):
    """
    Amazon Resource Name (ARN) of the workgroup
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block with various settings for the workgroup. Documented below.
    """
    configuration: Configuration | None = core.attr(Configuration, default=None)

    """
    (Optional) Description of the workgroup.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The option to delete the workgroup and its contents even if the workgroup contains any na
    med queries.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The workgroup name
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the workgroup.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
    """
    state: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags for the workgroup. If configured with a provider [`default
    _tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defaul
    t_tags-configuration-block) present, tags with matching keys will overwrite those defined at the pro
    vider-level.
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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        configuration: Configuration | None = None,
        description: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workgroup.Args(
                name=name,
                configuration=configuration,
                description=description,
                force_destroy=force_destroy,
                state=state,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Configuration | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
