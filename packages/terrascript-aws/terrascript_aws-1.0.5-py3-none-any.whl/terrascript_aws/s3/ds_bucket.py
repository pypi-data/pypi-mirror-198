import terrascript.core as core


@core.data(type="aws_s3_bucket", namespace="s3")
class DsBucket(core.Data):
    """
    The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the bucket
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.
    """
    bucket_domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The bucket region-specific domain name. The bucket domain name including the region name, please ref
    er [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The
    AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will preven
    t [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3
    Origin URL.
    """
    bucket_regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_re
    gion_endpoints) for this bucket's region.
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the bucket.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS region this bucket resides in.
    """
    region: str | core.StringOut = core.attr(str, computed=True)

    """
    The domain of the website endpoint, if the bucket is configured with a website. If not, this will be
    an empty string. This is used to create Route 53 alias records.
    """
    website_domain: str | core.StringOut = core.attr(str, computed=True)

    """
    The website endpoint, if the bucket is configured with a website. If not, this will be an empty stri
    ng.
    """
    website_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsBucket.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()
