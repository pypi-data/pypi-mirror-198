import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_ram_resource_share", namespace="ram")
class DsResourceShare(core.Data):
    """
    The Amazon Resource Name (ARN) of the resource share.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A filter used to scope the list e.g., by tags. See [related docs] (https://docs.aws.amazo
    n.com/ram/latest/APIReference/API_TagFilter.html).
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) of the resource share.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the resource share to retrieve.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The ID of the AWS account that owns the resource share.
    """
    owning_account_id: str | core.StringOut = core.attr(str, computed=True)

    resource_owner: str | core.StringOut = core.attr(str)

    resource_share_status: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Status of the RAM share.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The Tags attached to the RAM share
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        resource_owner: str | core.StringOut,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        resource_share_status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResourceShare.Args(
                name=name,
                resource_owner=resource_owner,
                filter=filter,
                resource_share_status=resource_share_status,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        resource_owner: str | core.StringOut = core.arg()

        resource_share_status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
