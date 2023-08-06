import terrascript.core as core


@core.resource(type="aws_simpledb_domain", namespace="sdb")
class SimpledbDomain(core.Resource):
    """
    The name of the SimpleDB domain
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the SimpleDB domain
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SimpledbDomain.Args(
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()
