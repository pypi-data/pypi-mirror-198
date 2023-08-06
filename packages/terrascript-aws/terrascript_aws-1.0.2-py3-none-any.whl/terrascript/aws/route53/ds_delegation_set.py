import terrascript.core as core


@core.data(type="aws_route53_delegation_set", namespace="aws_route53")
class DsDelegationSet(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str)

    name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDelegationSet.Args(
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()
