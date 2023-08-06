import terrascript.core as core


@core.schema
class IpSets(core.Schema):

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ip_family: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
        ip_family: str | core.StringOut,
    ):
        super().__init__(
            args=IpSets.Args(
                ip_addresses=ip_addresses,
                ip_family=ip_family,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        ip_family: str | core.StringOut = core.arg()


@core.schema
class Attributes(core.Schema):

    flow_logs_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    flow_logs_s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    flow_logs_s3_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        flow_logs_enabled: bool | core.BoolOut | None = None,
        flow_logs_s3_bucket: str | core.StringOut | None = None,
        flow_logs_s3_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Attributes.Args(
                flow_logs_enabled=flow_logs_enabled,
                flow_logs_s3_bucket=flow_logs_s3_bucket,
                flow_logs_s3_prefix=flow_logs_s3_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        flow_logs_enabled: bool | core.BoolOut | None = core.arg(default=None)

        flow_logs_s3_bucket: str | core.StringOut | None = core.arg(default=None)

        flow_logs_s3_prefix: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_globalaccelerator_accelerator", namespace="globalaccelerator")
class Accelerator(core.Resource):
    """
    (Optional) The attributes of the accelerator. Fields documented below.
    """

    attributes: Attributes | None = core.attr(Attributes, default=None)

    """
    The DNS name of the accelerator. For example, `a5d53ff5ee6bca4ce.awsglobalaccelerator.com`.
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether the accelerator is enabled. Defaults to `true`. Valid values: `true`, `
    false`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the accelerator.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The value for the address type. Defaults to `IPV4`. Valid values: `IPV4`, `DUAL_STACK`.
    """
    ip_address_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    IP address set associated with the accelerator.
    """
    ip_sets: list[IpSets] | core.ArrayOut[IpSets] = core.attr(
        IpSets, computed=True, kind=core.Kind.array
    )

    """
    (Required) The name of the accelerator.
    """
    name: str | core.StringOut = core.attr(str)

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
        name: str | core.StringOut,
        attributes: Attributes | None = None,
        enabled: bool | core.BoolOut | None = None,
        ip_address_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Accelerator.Args(
                name=name,
                attributes=attributes,
                enabled=enabled,
                ip_address_type=ip_address_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attributes: Attributes | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        ip_address_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
