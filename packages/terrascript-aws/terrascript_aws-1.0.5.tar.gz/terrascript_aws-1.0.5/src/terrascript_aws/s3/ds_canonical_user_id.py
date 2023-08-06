import terrascript.core as core


@core.data(type="aws_canonical_user_id", namespace="s3")
class DsCanonicalUserId(core.Data):
    """
    The human-friendly name linked to the canonical user ID. The bucket owner's display name. **NOTE:**
    [This value](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTServiceGET.html) is only included i
    n the response in the US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific
    (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), EU (Ireland), and South America (São Paul
    o) regions.
    """

    display_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The canonical user ID associated with the AWS account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsCanonicalUserId.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
