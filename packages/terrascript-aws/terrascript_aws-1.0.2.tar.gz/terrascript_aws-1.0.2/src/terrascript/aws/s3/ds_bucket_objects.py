import terrascript.core as core


@core.data(type="aws_s3_bucket_objects", namespace="aws_s3")
class DsBucketObjects(core.Data):

    bucket: str | core.StringOut = core.attr(str)

    common_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    delimiter: str | core.StringOut | None = core.attr(str, default=None)

    encoding_type: str | core.StringOut | None = core.attr(str, default=None)

    fetch_owner: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    keys: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_keys: int | core.IntOut | None = core.attr(int, default=None)

    owners: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    prefix: str | core.StringOut | None = core.attr(str, default=None)

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
