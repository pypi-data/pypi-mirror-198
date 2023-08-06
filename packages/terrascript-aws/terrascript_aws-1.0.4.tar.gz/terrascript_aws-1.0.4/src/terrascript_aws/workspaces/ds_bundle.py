import terrascript.core as core


@core.schema
class RootStorage(core.Schema):

    capacity: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        capacity: str | core.StringOut,
    ):
        super().__init__(
            args=RootStorage.Args(
                capacity=capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity: str | core.StringOut = core.arg()


@core.schema
class ComputeType(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=ComputeType.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class UserStorage(core.Schema):

    capacity: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        capacity: str | core.StringOut,
    ):
        super().__init__(
            args=UserStorage.Args(
                capacity=capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity: str | core.StringOut = core.arg()


@core.data(type="aws_workspaces_bundle", namespace="workspaces")
class DsBundle(core.Data):

    bundle_id: str | core.StringOut | None = core.attr(str, default=None)

    compute_type: list[ComputeType] | core.ArrayOut[ComputeType] = core.attr(
        ComputeType, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the compute type.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    owner: str | core.StringOut | None = core.attr(str, default=None)

    root_storage: list[RootStorage] | core.ArrayOut[RootStorage] = core.attr(
        RootStorage, computed=True, kind=core.Kind.array
    )

    user_storage: list[UserStorage] | core.ArrayOut[UserStorage] = core.attr(
        UserStorage, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        bundle_id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        owner: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBundle.Args(
                bundle_id=bundle_id,
                name=name,
                owner=owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bundle_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        owner: str | core.StringOut | None = core.arg(default=None)
