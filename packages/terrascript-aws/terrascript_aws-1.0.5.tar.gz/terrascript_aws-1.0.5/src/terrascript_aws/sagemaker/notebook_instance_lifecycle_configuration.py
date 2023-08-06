import terrascript.core as core


@core.resource(
    type="aws_sagemaker_notebook_instance_lifecycle_configuration", namespace="sagemaker"
)
class NotebookInstanceLifecycleConfiguration(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this lifecycle configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the lifecycle configuration (must be unique). If omitted, Terraform will assi
    gn a random, unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance
    is created.
    """
    on_create: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is s
    tarted including the time it's created.
    """
    on_start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut | None = None,
        on_create: str | core.StringOut | None = None,
        on_start: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NotebookInstanceLifecycleConfiguration.Args(
                name=name,
                on_create=on_create,
                on_start=on_start,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        on_create: str | core.StringOut | None = core.arg(default=None)

        on_start: str | core.StringOut | None = core.arg(default=None)
