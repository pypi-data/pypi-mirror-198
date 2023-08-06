import terrascript.core as core


@core.data(type="aws_cloudwatch_log_groups", namespace="cloudwatch")
class DsLogGroups(core.Data):
    """
    Set of ARNs of the Cloudwatch log groups
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The group prefix of the Cloudwatch log groups to list
    """
    log_group_name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    Set of names of the Cloudwatch log groups
    """
    log_group_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        log_group_name_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLogGroups.Args(
                log_group_name_prefix=log_group_name_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name_prefix: str | core.StringOut | None = core.arg(default=None)
