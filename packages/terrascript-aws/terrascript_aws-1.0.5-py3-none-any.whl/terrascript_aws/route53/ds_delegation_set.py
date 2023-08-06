import terrascript.core as core


@core.data(type="aws_route53_delegation_set", namespace="route53")
class DsDelegationSet(core.Data):
    """
    The Amazon Resource Name (ARN) of the Delegation Set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Caller Reference of the delegation set.
    """
    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Hosted Zone id of the desired delegation set.
    """
    id: str | core.StringOut = core.attr(str)

    """
    The list of DNS name servers for the delegation set.
    """
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
