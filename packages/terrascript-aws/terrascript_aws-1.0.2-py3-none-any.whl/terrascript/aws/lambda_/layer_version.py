import terrascript.core as core


@core.resource(type="aws_lambda_layer_version", namespace="aws_lambda_")
class LayerVersion(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    compatible_architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    compatible_runtimes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    filename: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    layer_arn: str | core.StringOut = core.attr(str, computed=True)

    layer_name: str | core.StringOut = core.attr(str)

    license_info: str | core.StringOut | None = core.attr(str, default=None)

    s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    s3_key: str | core.StringOut | None = core.attr(str, default=None)

    s3_object_version: str | core.StringOut | None = core.attr(str, default=None)

    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    skip_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    source_code_hash: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        layer_name: str | core.StringOut,
        compatible_architectures: list[str] | core.ArrayOut[core.StringOut] | None = None,
        compatible_runtimes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        filename: str | core.StringOut | None = None,
        license_info: str | core.StringOut | None = None,
        s3_bucket: str | core.StringOut | None = None,
        s3_key: str | core.StringOut | None = None,
        s3_object_version: str | core.StringOut | None = None,
        skip_destroy: bool | core.BoolOut | None = None,
        source_code_hash: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LayerVersion.Args(
                layer_name=layer_name,
                compatible_architectures=compatible_architectures,
                compatible_runtimes=compatible_runtimes,
                description=description,
                filename=filename,
                license_info=license_info,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_object_version=s3_object_version,
                skip_destroy=skip_destroy,
                source_code_hash=source_code_hash,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compatible_architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        compatible_runtimes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        description: str | core.StringOut | None = core.arg(default=None)

        filename: str | core.StringOut | None = core.arg(default=None)

        layer_name: str | core.StringOut = core.arg()

        license_info: str | core.StringOut | None = core.arg(default=None)

        s3_bucket: str | core.StringOut | None = core.arg(default=None)

        s3_key: str | core.StringOut | None = core.arg(default=None)

        s3_object_version: str | core.StringOut | None = core.arg(default=None)

        skip_destroy: bool | core.BoolOut | None = core.arg(default=None)

        source_code_hash: str | core.StringOut | None = core.arg(default=None)
