import terrascript.core as core


@core.schema
class Rule(core.Schema):

    attribute: str | core.StringOut | None = core.attr(str, default=None)

    operator: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        attribute: str | core.StringOut | None = None,
        operator: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                attribute=attribute,
                operator=operator,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attribute: str | core.StringOut | None = core.arg(default=None)

        operator: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_devicefarm_device_pool", namespace="devicefarm")
class DevicePool(core.Resource):
    """
    The Amazon Resource Name of this Device Pool
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The device pool's description.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of devices that Device Farm can add to your device pool.
    """
    max_devices: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The name of the Device Pool
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of the project for the device pool.
    """
    project_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The device pool's rules. See [Rule](#rule).
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        project_arn: str | core.StringOut,
        rule: list[Rule] | core.ArrayOut[Rule],
        description: str | core.StringOut | None = None,
        max_devices: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DevicePool.Args(
                name=name,
                project_arn=project_arn,
                rule=rule,
                description=description,
                max_devices=max_devices,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        max_devices: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        project_arn: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
