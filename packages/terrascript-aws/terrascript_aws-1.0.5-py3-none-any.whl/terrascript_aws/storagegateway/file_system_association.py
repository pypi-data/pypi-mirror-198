import terrascript.core as core


@core.schema
class CacheAttributes(core.Schema):

    cache_stale_timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CacheAttributes.Args(
                cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cache_stale_timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_storagegateway_file_system_association", namespace="storagegateway")
class FileSystemAssociation(core.Resource):
    """
    Amazon Resource Name (ARN) of the newly created file system association.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the storage used for the audit logs.
    """
    audit_destination_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Refresh cache information. see [Cache Attributes](#cache_attributes) for more details.
    """
    cache_attributes: CacheAttributes | None = core.attr(CacheAttributes, default=None)

    """
    (Required) The Amazon Resource Name (ARN) of the gateway.
    """
    gateway_arn: str | core.StringOut = core.attr(str)

    """
    Amazon Resource Name (ARN) of the FSx file system association
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the Amazon FSx file system to associate with the FSx Fi
    le Gateway.
    """
    location_arn: str | core.StringOut = core.attr(str)

    """
    (Required, sensitive) The password of the user credential.
    """
    password: str | core.StringOut = core.attr(str)

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

    """
    (Required) The user name of the user credential that has permission to access the root share of the
    Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.
    """
    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: str | core.StringOut,
        location_arn: str | core.StringOut,
        password: str | core.StringOut,
        username: str | core.StringOut,
        audit_destination_arn: str | core.StringOut | None = None,
        cache_attributes: CacheAttributes | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FileSystemAssociation.Args(
                gateway_arn=gateway_arn,
                location_arn=location_arn,
                password=password,
                username=username,
                audit_destination_arn=audit_destination_arn,
                cache_attributes=cache_attributes,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audit_destination_arn: str | core.StringOut | None = core.arg(default=None)

        cache_attributes: CacheAttributes | None = core.arg(default=None)

        gateway_arn: str | core.StringOut = core.arg()

        location_arn: str | core.StringOut = core.arg()

        password: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        username: str | core.StringOut = core.arg()
