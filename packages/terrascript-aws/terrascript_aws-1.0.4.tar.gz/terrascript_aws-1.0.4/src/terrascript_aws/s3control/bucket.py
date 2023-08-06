import terrascript.core as core


@core.resource(type="aws_s3control_bucket", namespace="s3control")
class Bucket(core.Resource):
    """
    Amazon Resource Name (ARN) of the bucket.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the bucket.
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    UTC creation date in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the bucket.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Identifier of the Outpost to contain this bucket.
    """
    outpost_id: str | core.StringOut = core.attr(str)

    """
    Boolean whether Public Access Block is enabled.
    """
    public_access_block_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

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
        bucket: str | core.StringOut,
        outpost_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Bucket.Args(
                bucket=bucket,
                outpost_id=outpost_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        outpost_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
