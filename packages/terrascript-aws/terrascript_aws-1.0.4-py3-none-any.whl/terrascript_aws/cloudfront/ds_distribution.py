import terrascript.core as core


@core.data(type="aws_cloudfront_distribution", namespace="cloudfront")
class DsDistribution(core.Data):
    """
    A list that contains information about CNAMEs (alternate domain names), if any, for this distributio
    n.
    """

    aliases: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:d
    istribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The domain name corresponding to the distribution. For
    """
    domain_name: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The current version of the distribution's information. For example:
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    The CloudFront Route 53 zone ID that can be used to
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the distribution. For example: `EDFDVBD632BHDS5`.
    """
    id: str | core.StringOut = core.attr(str)

    """
    The number of invalidation batches
    """
    in_progress_validation_batches: int | core.IntOut = core.attr(int, computed=True)

    """
    The date and time the distribution was last modified.
    """
    last_modified_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The current status of the distribution. `Deployed` if the
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDistribution.Args(
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
