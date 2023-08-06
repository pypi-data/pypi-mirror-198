import terrascript.core as core


@core.resource(type="aws_dax_subnet_group", namespace="dynamodb_accelerator")
class DaxSubnetGroup(core.Resource):
    """
    (Optional) A description of the subnet group.
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the subnet group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DaxSubnetGroup.Args(
                name=name,
                subnet_ids=subnet_ids,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()
