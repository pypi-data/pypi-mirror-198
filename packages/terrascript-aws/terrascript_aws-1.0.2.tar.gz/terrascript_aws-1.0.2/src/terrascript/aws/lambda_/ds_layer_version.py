import terrascript.core as core


@core.data(type="aws_lambda_layer_version", namespace="aws_lambda_")
class DsLayerVersion(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    compatible_architecture: str | core.StringOut | None = core.attr(str, default=None)

    compatible_architectures: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    compatible_runtime: str | core.StringOut | None = core.attr(str, default=None)

    compatible_runtimes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    layer_arn: str | core.StringOut = core.attr(str, computed=True)

    layer_name: str | core.StringOut = core.attr(str)

    license_info: str | core.StringOut = core.attr(str, computed=True)

    signing_job_arn: str | core.StringOut = core.attr(str, computed=True)

    signing_profile_version_arn: str | core.StringOut = core.attr(str, computed=True)

    source_code_hash: str | core.StringOut = core.attr(str, computed=True)

    source_code_size: int | core.IntOut = core.attr(int, computed=True)

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
