import terrascript.core as core


@core.resource(
    type="aws_serverlessapplicationrepository_cloudformation_stack",
    namespace="serverlessapplicationrepository",
)
class CloudformationStack(core.Resource):
    """
    (Required) The ARN of the application from the Serverless Application Repository.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    (Required) A list of capabilities. Valid values are `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPAB
    ILITY_RESOURCE_POLICY`, or `CAPABILITY_AUTO_EXPAND`
    """
    capabilities: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    A unique identifier of the stack.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the stack to create. The resource deployed in AWS will be prefixed with `serv
    erlessrepo-`
    """
    name: str | core.StringOut = core.attr(str)

    """
    A map of outputs from the stack.
    """
    outputs: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    (Optional) A map of Parameter structures that specify input parameters for the stack.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) The version of the application to deploy. If not supplied, deploys the latest version.
    """
    semantic_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of tags to associate with this stack. If configured with a provider [`default_tags
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tag
    s-configuration-block) present, tags with matching keys will overwrite those defined at the provider
    level.
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
        application_id: str | core.StringOut,
        capabilities: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        semantic_version: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudformationStack.Args(
                application_id=application_id,
                capabilities=capabilities,
                name=name,
                parameters=parameters,
                semantic_version=semantic_version,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        capabilities: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        semantic_version: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
