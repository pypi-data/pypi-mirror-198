import terrascript.core as core


@core.data(type="aws_s3_bucket_objects", namespace="s3")
class DsBucketObjects(core.Data):
    """
    (Required) Lists object keys in this S3 bucket. Alternatively, an [S3 access point](https://docs.aws
    .amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    List of any keys between `prefix` and the next occurrence of `delimiter` (i.e., similar to subdirect
    ories of the `prefix` "directory"); the list is only returned when you specify `delimiter`
    """
    common_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A character used to group keys (Default: none)
    """
    delimiter: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Encodes keys using this method (Default: none; besides none, only "url" can be used)
    """
    encoding_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Boolean specifying whether to populate the owner list (Default: false)
    """
    fetch_owner: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    S3 Bucket.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of strings representing object keys
    """
    keys: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Maximum object keys to return (Default: 1000)
    """
    max_keys: int | core.IntOut | None = core.attr(int, default=None)

    """
    List of strings representing object owner IDs (see `fetch_owner` above)
    """
    owners: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Limits results to object keys with this prefix (Default: none)
    """
    prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Returns key names lexicographically after a specific object key in your bucket (Default:
    none; S3 lists object keys in UTF-8 character encoding in lexicographical order)
    """
    start_after: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: str | core.StringOut,
        delimiter: str | core.StringOut | None = None,
        encoding_type: str | core.StringOut | None = None,
        fetch_owner: bool | core.BoolOut | None = None,
        max_keys: int | core.IntOut | None = None,
        prefix: str | core.StringOut | None = None,
        start_after: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBucketObjects.Args(
                bucket=bucket,
                delimiter=delimiter,
                encoding_type=encoding_type,
                fetch_owner=fetch_owner,
                max_keys=max_keys,
                prefix=prefix,
                start_after=start_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        delimiter: str | core.StringOut | None = core.arg(default=None)

        encoding_type: str | core.StringOut | None = core.arg(default=None)

        fetch_owner: bool | core.BoolOut | None = core.arg(default=None)

        max_keys: int | core.IntOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        start_after: str | core.StringOut | None = core.arg(default=None)
