import terrascript.core as core


@core.data(type="aws_outposts_outpost_instance_types", namespace="outposts")
class DsOutpostInstanceTypes(core.Data):
    """
    (Required) Outpost Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of instance types.
    """
    instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsOutpostInstanceTypes.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()
