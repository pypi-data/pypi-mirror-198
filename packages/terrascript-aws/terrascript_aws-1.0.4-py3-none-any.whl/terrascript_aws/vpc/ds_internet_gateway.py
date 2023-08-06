import terrascript.core as core


@core.schema
class Attachments(core.Schema):

    state: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        state: str | core.StringOut,
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=Attachments.Args(
                state=state,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        state: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()


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


@core.data(type="aws_internet_gateway", namespace="vpc")
class DsInternetGateway(core.Data):
    """
    The ARN of the Internet Gateway.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    attachments: list[Attachments] | core.ArrayOut[Attachments] = core.attr(
        Attachments, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Custom filter block as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The id of the specific Internet Gateway to retrieve.
    """
    internet_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the AWS account that owns the internet gateway.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        internet_gateway_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInternetGateway.Args(
                filter=filter,
                internet_gateway_id=internet_gateway_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        internet_gateway_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
