import terrascript.core as core


@core.schema
class UiTemplate(core.Schema):

    content: str | core.StringOut | None = core.attr(str, default=None)

    content_sha256: str | core.StringOut = core.attr(str, computed=True)

    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        content_sha256: str | core.StringOut,
        url: str | core.StringOut,
        content: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=UiTemplate.Args(
                content_sha256=content_sha256,
                url=url,
                content=content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: str | core.StringOut | None = core.arg(default=None)

        content_sha256: str | core.StringOut = core.arg()

        url: str | core.StringOut = core.arg()


@core.resource(type="aws_sagemaker_human_task_ui", namespace="sagemaker")
class HumanTaskUi(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Human Task UI.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Human Task UI.
    """
    human_task_ui_name: str | core.StringOut = core.attr(str)

    """
    The name of the Human Task UI.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

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

    """
    (Required) The Liquid template for the worker user interface. See [UI Template](#ui-template) below.
    """
    ui_template: UiTemplate = core.attr(UiTemplate)

    def __init__(
        self,
        resource_name: str,
        *,
        human_task_ui_name: str | core.StringOut,
        ui_template: UiTemplate,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HumanTaskUi.Args(
                human_task_ui_name=human_task_ui_name,
                ui_template=ui_template,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        human_task_ui_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        ui_template: UiTemplate = core.arg()
