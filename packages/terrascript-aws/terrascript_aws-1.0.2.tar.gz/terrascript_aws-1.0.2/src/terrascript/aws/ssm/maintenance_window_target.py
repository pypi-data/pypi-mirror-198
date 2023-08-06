import terrascript.core as core


@core.schema
class Targets(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Targets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_ssm_maintenance_window_target", namespace="aws_ssm")
class MaintenanceWindowTarget(core.Resource):

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None)

    owner_information: str | core.StringOut | None = core.attr(str, default=None)

    resource_type: str | core.StringOut = core.attr(str)

    targets: list[Targets] | core.ArrayOut[Targets] = core.attr(Targets, kind=core.Kind.array)

    window_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_type: str | core.StringOut,
        targets: list[Targets] | core.ArrayOut[Targets],
        window_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        owner_information: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MaintenanceWindowTarget.Args(
                resource_type=resource_type,
                targets=targets,
                window_id=window_id,
                description=description,
                name=name,
                owner_information=owner_information,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        owner_information: str | core.StringOut | None = core.arg(default=None)

        resource_type: str | core.StringOut = core.arg()

        targets: list[Targets] | core.ArrayOut[Targets] = core.arg()

        window_id: str | core.StringOut = core.arg()
