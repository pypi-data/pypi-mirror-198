import terrascript.core as core


@core.data(type="aws_memorydb_acl", namespace="memorydb")
class DsAcl(core.Data):
    """
    ARN of the ACL.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the ACL.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The minimum engine version supported by the ACL.
    """
    minimum_engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the ACL.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A map of tags assigned to the ACL.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Set of MemoryDB user names included in this ACL.
    """
    user_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAcl.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
