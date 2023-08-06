import terrascript.core as core


@core.resource(type="aws_lambda_layer_version", namespace="lambda_")
class LayerVersion(core.Resource):
    """
    ARN of the Lambda Layer with version.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of [Architectures][4] this layer is compatible with. Currently `x86_64` and `arm64`
    can be specified.
    """
    compatible_architectures: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
    """
    compatible_runtimes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Date this resource was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of what your Lambda Layer does.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    filename: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the Lambda Layer without version.
    """
    layer_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique name for your Lambda Layer
    """
    layer_name: str | core.StringOut = core.attr(str)

    """
    (Optional) License info for your Lambda Layer. See [License Info][3].
    """
    license_info: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 bucket location containing the function's deployment package. Conflicts with `filename
    . This bucket must reside in the same AWS region where you are creating the Lambda function.
    """
    s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) S3 key of an object containing the function's deployment package. Conflicts with `filenam
    e`.
    """
    s3_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Object version containing the function's deployment package. Conflicts with `filename`.
    """
    s3_object_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    ARN of a signing job.
    """
    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN for a signing profile version.
    """
    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to retain the old version of a previously deployed Lambda Layer. Default is `fals
    e`. When this is not set to `true`, changing any of `compatible_architectures`, `compatible_runtimes
    , `description`, `filename`, `layer_name`, `license_info`, `s3_bucket`, `s3_key`, `s3_object_versio
    n`, or `source_code_hash` forces deletion of the existing layer version and creation of a new layer
    version.
    """
    skip_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file
    specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256("file
    .zip")}` (Terraform 0.11.12 or later) or `${base64sha256(file("file.zip"))}` (Terraform 0.11.11 and
    earlier), where "file.zip" is the local filename of the lambda layer source archive.
    """
    source_code_hash: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Size in bytes of the function .zip file.
    """
    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    """
    Lambda Layer version.
    """
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
