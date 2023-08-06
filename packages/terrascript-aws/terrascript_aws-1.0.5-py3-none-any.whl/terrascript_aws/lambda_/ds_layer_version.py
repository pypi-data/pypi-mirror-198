import terrascript.core as core


@core.data(type="aws_lambda_layer_version", namespace="lambda_")
class DsLayerVersion(core.Data):
    """
    The Amazon Resource Name (ARN) of the Lambda Layer with version.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    compatible_architecture: str | core.StringOut | None = core.attr(str, default=None)

    """
    A list of [Architectures][2] the specific Lambda Layer version is compatible with.
    """
    compatible_architectures: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compatible_runtime: str | core.StringOut | None = core.attr(str, default=None)

    """
    A list of [Runtimes][1] the specific Lambda Layer version is compatible with.
    """
    compatible_runtimes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The date this resource was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the specific Lambda Layer version.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the Lambda Layer without version.
    """
    layer_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the lambda layer.
    """
    layer_name: str | core.StringOut = core.attr(str)

    """
    License info associated with the specific Lambda Layer version.
    """
    license_info: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of a signing job.
    """
    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) for a signing profile version.
    """
    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Base64-encoded representation of raw SHA-256 sum of the zip file.
    """
    source_code_hash: str | core.StringOut = core.attr(str, computed=True)

    """
    The size in bytes of the function .zip file.
    """
    source_code_size: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Specific layer version. Conflicts with `compatible_runtime` and `compatible_architecture`
    . If omitted, the latest available layer version will be used.
    """
    version: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        layer_name: str | core.StringOut,
        compatible_architecture: str | core.StringOut | None = None,
        compatible_runtime: str | core.StringOut | None = None,
        version: int | core.IntOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLayerVersion.Args(
                layer_name=layer_name,
                compatible_architecture=compatible_architecture,
                compatible_runtime=compatible_runtime,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compatible_architecture: str | core.StringOut | None = core.arg(default=None)

        compatible_runtime: str | core.StringOut | None = core.arg(default=None)

        layer_name: str | core.StringOut = core.arg()

        version: int | core.IntOut | None = core.arg(default=None)
