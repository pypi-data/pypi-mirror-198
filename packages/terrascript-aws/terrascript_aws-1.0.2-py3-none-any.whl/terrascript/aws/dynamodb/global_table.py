import terrascript.core as core


@core.schema
class Replica(core.Schema):

    region_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        region_name: str | core.StringOut,
    ):
        super().__init__(
            args=Replica.Args(
                region_name=region_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region_name: str | core.StringOut = core.arg()


@core.resource(type="aws_dynamodb_global_table", namespace="aws_dynamodb")
class GlobalTable(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    replica: list[Replica] | core.ArrayOut[Replica] = core.attr(Replica, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        replica: list[Replica] | core.ArrayOut[Replica],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalTable.Args(
                name=name,
                replica=replica,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        replica: list[Replica] | core.ArrayOut[Replica] = core.arg()
