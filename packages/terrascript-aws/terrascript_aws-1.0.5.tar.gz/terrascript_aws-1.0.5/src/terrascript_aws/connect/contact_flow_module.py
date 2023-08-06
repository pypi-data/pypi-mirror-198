import terrascript.core as core


@core.resource(type="aws_connect_contact_flow_module", namespace="connect")
class ContactFlowModule(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Contact Flow Module.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the Contact Flow Module.
    """
    contact_flow_module_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the content of the Contact Flow Module, provided as a JSON string, written in A
    mazon Connect Contact Flow Language. If defined, the `filename` argument cannot be used.
    """
    content: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the Contact Flow
    Module source specified with `filename`. The usual way to set this is filebase64sha256("contact_flow
    _module.json") (Terraform 0.11.12 and later) or base64sha256(file("contact_flow_module.json")) (Terr
    aform 0.11.11 and earlier), where "contact_flow_module.json" is the local filename of the Contact Fl
    ow Module source.
    """
    content_hash: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the description of the Contact Flow Module.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The path to the Contact Flow Module source within the local filesystem. Conflicts with `c
    ontent`.
    """
    filename: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Contact Flow Module sepa
    rated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the name of the Contact Flow Module.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Tags to apply to the Contact Flow Module. If configured with a provider [`default_tags` c
    onfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-c
    onfiguration-block) present, tags with matching keys will overwrite those defined at the provider-le
    vel.
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
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
        content: str | core.StringOut | None = None,
        content_hash: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        filename: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContactFlowModule.Args(
                instance_id=instance_id,
                name=name,
                content=content,
                content_hash=content_hash,
                description=description,
                filename=filename,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content: str | core.StringOut | None = core.arg(default=None)

        content_hash: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        filename: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
