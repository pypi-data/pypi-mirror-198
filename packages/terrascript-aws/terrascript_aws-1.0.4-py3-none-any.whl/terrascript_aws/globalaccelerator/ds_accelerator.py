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

    flow_logs_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    flow_logs_s3_bucket: str | core.StringOut = core.attr(str, computed=True)

    flow_logs_s3_prefix: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        flow_logs_enabled: bool | core.BoolOut,
        flow_logs_s3_bucket: str | core.StringOut,
        flow_logs_s3_prefix: str | core.StringOut,
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
        flow_logs_enabled: bool | core.BoolOut = core.arg()

        flow_logs_s3_bucket: str | core.StringOut = core.arg()

        flow_logs_s3_prefix: str | core.StringOut = core.arg()


@core.data(type="aws_globalaccelerator_accelerator", namespace="globalaccelerator")
class DsAccelerator(core.Data):
    """
    (Optional) The full ARN of the Global Accelerator.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    attributes: list[Attributes] | core.ArrayOut[Attributes] = core.attr(
        Attributes, computed=True, kind=core.Kind.array
    )

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address_type: str | core.StringOut = core.attr(str, computed=True)

    ip_sets: list[IpSets] | core.ArrayOut[IpSets] = core.attr(
        IpSets, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The unique name of the Global Accelerator.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAccelerator.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
