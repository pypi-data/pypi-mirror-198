import terrascript.core as core


@core.resource(type="aws_codedeploy_app", namespace="codedeploy")
class App(core.Resource):
    """
    The application ID.
    """

    application_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the CodeDeploy application.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The compute platform can either be `ECS`, `Lambda`, or `Server`. Default is `Server`.
    """
    compute_platform: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name for a connection to a GitHub account.
    """
    github_account_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon's assigned ID for the application.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the user has authenticated with GitHub for the specified application.
    """
    linked_to_github: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) The name of the application.
    """
    name: str | core.StringOut = core.attr(str)

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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        compute_platform: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=App.Args(
                name=name,
                compute_platform=compute_platform,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_platform: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
