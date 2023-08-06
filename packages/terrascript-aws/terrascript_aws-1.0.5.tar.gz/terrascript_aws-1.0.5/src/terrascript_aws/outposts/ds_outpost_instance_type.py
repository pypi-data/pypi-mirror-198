import terrascript.core as core


@core.data(type="aws_outposts_outpost_instance_type", namespace="outposts")
class DsOutpostInstanceType(core.Data):
    """
    (Required) Outpost Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Outpost identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Desired instance type. Conflicts with `preferred_instance_types`.
    """
    instance_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Ordered list of preferred instance types. The first match in this list will be returned.
    If no preferred matches are found and the original search returned more than one result, an error is
    returned. Conflicts with `instance_type`.
    """
    preferred_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        instance_type: str | core.StringOut | None = None,
        preferred_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutpostInstanceType.Args(
                arn=arn,
                instance_type=instance_type,
                preferred_instance_types=preferred_instance_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        instance_type: str | core.StringOut | None = core.arg(default=None)

        preferred_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
