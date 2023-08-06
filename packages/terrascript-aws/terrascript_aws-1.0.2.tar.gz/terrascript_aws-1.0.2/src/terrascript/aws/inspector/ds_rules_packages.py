import terrascript.core as core


@core.data(type="aws_inspector_rules_packages", namespace="aws_inspector")
class DsRulesPackages(core.Data):

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsRulesPackages.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
