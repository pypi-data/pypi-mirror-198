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


@core.resource(type="aws_ssm_maintenance_window_target", namespace="ssm")
class MaintenanceWindowTarget(core.Resource):
    """
    (Optional) The description of the maintenance window target.
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the maintenance window target.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the maintenance window target.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) User-provided value that will be included in any CloudWatch events raised while running t
    asks for these targets in this Maintenance Window.
    """
    owner_information: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of target being registered with the Maintenance Window. Possible values are `INS
    TANCE` and `RESOURCE_GROUP`.
    """
    resource_type: str | core.StringOut = core.attr(str)

    """
    (Required) The targets to register with the maintenance window. In other words, the instances to run
    commands on when the maintenance window runs. You can specify targets using instance IDs, resource
    group names, or tags that have been applied to instances. For more information about these examples
    formats see
    """
    targets: list[Targets] | core.ArrayOut[Targets] = core.attr(Targets, kind=core.Kind.array)

    """
    (Required) The Id of the maintenance window to register the target with.
    """
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
