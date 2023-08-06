import terrascript.core as core


@core.schema
class EksInfo(core.Schema):

    namespace: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        namespace: str | core.StringOut,
    ):
        super().__init__(
            args=EksInfo.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: str | core.StringOut = core.arg()


@core.schema
class Info(core.Schema):

    eks_info: list[EksInfo] | core.ArrayOut[EksInfo] = core.attr(
        EksInfo, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        eks_info: list[EksInfo] | core.ArrayOut[EksInfo],
    ):
        super().__init__(
            args=Info.Args(
                eks_info=eks_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eks_info: list[EksInfo] | core.ArrayOut[EksInfo] = core.arg()


@core.schema
class ContainerProvider(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    info: list[Info] | core.ArrayOut[Info] = core.attr(Info, computed=True, kind=core.Kind.array)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        info: list[Info] | core.ArrayOut[Info],
        type: str | core.StringOut,
    ):
        super().__init__(
            args=ContainerProvider.Args(
                id=id,
                info=info,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        info: list[Info] | core.ArrayOut[Info] = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_emrcontainers_virtual_cluster", namespace="emrcontainers")
class DsVirtualCluster(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    container_provider: list[ContainerProvider] | core.ArrayOut[ContainerProvider] = core.attr(
        ContainerProvider, computed=True, kind=core.Kind.array
    )

    created_at: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    virtual_cluster_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        virtual_cluster_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsVirtualCluster.Args(
                virtual_cluster_id=virtual_cluster_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        virtual_cluster_id: str | core.StringOut = core.arg()
