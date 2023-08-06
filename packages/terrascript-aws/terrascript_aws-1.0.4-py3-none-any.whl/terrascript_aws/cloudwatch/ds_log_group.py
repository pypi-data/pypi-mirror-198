import terrascript.core as core


@core.data(type="aws_cloudwatch_log_group", namespace="cloudwatch")
class DsLogGroup(core.Data):
    """
    The ARN of the Cloudwatch log group. Any `:*` suffix added by the API, denoting all CloudWatch Log S
    treams under the CloudWatch Log Group, is removed for greater compatibility with other AWS services
    that do not accept the suffix.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:
    00 UTC.
    """
    creation_time: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the KMS Key to use when encrypting log data.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Cloudwatch log group
    """
    name: str | core.StringOut = core.attr(str)

    """
    The number of days log events retained in the specified log group.
    """
    retention_in_days: int | core.IntOut = core.attr(int, computed=True)

    """
    A map of tags to assign to the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLogGroup.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
