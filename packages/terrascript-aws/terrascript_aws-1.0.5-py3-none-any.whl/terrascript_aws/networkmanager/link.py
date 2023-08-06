import terrascript.core as core


@core.schema
class Bandwidth(core.Schema):

    download_speed: int | core.IntOut | None = core.attr(int, default=None)

    upload_speed: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        download_speed: int | core.IntOut | None = None,
        upload_speed: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Bandwidth.Args(
                download_speed=download_speed,
                upload_speed=upload_speed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        download_speed: int | core.IntOut | None = core.arg(default=None)

        upload_speed: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_networkmanager_link", namespace="networkmanager")
class Link(core.Resource):
    """
    Link Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The upload speed and download speed in Mbps. Documented below.
    """
    bandwidth: Bandwidth = core.attr(Bandwidth)

    """
    (Optional) A description of the link.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the global network.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The provider of the link.
    """
    provider_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the site.
    """
    site_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value tags for the link. If configured with a provider [`default_tags` configuration
    block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-
    block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) The type of the link.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: Bandwidth,
        global_network_id: str | core.StringOut,
        site_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        provider_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Link.Args(
                bandwidth=bandwidth,
                global_network_id=global_network_id,
                site_id=site_id,
                description=description,
                provider_name=provider_name,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: Bandwidth = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        global_network_id: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut | None = core.arg(default=None)

        site_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
