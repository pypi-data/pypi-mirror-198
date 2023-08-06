import terrascript.core as core


@core.data(type="aws_ssoadmin_instances", namespace="aws_ssoadmin")
class DsInstances(core.Data):

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

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
