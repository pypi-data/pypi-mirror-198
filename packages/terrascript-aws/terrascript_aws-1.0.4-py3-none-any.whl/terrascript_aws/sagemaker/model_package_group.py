import terrascript.core as core


@core.resource(type="aws_sagemaker_model_package_group", namespace="sagemaker")
class ModelPackageGroup(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Model Package Group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the Model Package Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description for the model group.
    """
    model_package_group_description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the model group.
    """
    model_package_group_name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
        model_package_group_name: str | core.StringOut,
        model_package_group_description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ModelPackageGroup.Args(
                model_package_group_name=model_package_group_name,
                model_package_group_description=model_package_group_description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        model_package_group_description: str | core.StringOut | None = core.arg(default=None)

        model_package_group_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
