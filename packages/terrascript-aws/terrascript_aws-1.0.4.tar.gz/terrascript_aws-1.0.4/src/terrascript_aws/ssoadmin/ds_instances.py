import terrascript.core as core


@core.data(type="aws_ssoadmin_instances", namespace="ssoadmin")
class DsInstances(core.Data):
    """
    Set of Amazon Resource Names (ARNs) of the SSO Instances.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    AWS Region.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of identifiers of the identity stores connected to the SSO Instances.
    """
    identity_store_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsInstances.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
