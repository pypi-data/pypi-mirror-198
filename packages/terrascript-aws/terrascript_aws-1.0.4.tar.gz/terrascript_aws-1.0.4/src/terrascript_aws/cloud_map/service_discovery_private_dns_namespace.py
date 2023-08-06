import terrascript.core as core


@core.resource(type="aws_service_discovery_private_dns_namespace", namespace="cloud_map")
class ServiceDiscoveryPrivateDnsNamespace(core.Resource):
    """
    The ARN that Amazon Route 53 assigns to the namespace when you create it.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description that you specify for the namespace when you create it.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
    """
    hosted_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of a namespace.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the namespace.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the namespace. If configured with a provider [`default_tags` c
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

    """
    (Required) The ID of VPC that you want to associate the namespace with.
    """
    vpc: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        vpc: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceDiscoveryPrivateDnsNamespace.Args(
                name=name,
                vpc=vpc,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc: str | core.StringOut = core.arg()
