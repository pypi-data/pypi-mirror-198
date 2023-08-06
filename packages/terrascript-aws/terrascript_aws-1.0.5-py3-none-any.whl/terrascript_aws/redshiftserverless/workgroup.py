import terrascript.core as core


@core.schema
class ConfigParameter(core.Schema):

    parameter_key: str | core.StringOut = core.attr(str)

    parameter_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        parameter_key: str | core.StringOut,
        parameter_value: str | core.StringOut,
    ):
        super().__init__(
            args=ConfigParameter.Args(
                parameter_key=parameter_key,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_key: str | core.StringOut = core.arg()

        parameter_value: str | core.StringOut = core.arg()


@core.resource(type="aws_redshiftserverless_workgroup", namespace="redshiftserverless")
class Workgroup(core.Resource):
    """
    Amazon Resource Name (ARN) of the Redshift Serverless Workgroup.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
    """
    base_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) An array of parameters to set for more control over a serverless database. See `Config Pa
    rameter` below.
    """
    config_parameter: list[ConfigParameter] | core.ArrayOut[ConfigParameter] | None = core.attr(
        ConfigParameter, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing,
    which forces Amazon Redshift Serverless to route traffic through your VPC instead of over the inter
    net.
    """
    enhanced_vpc_routing: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Redshift Workgroup Name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    namespace_name: str | core.StringOut = core.attr(str)

    """
    (Optional) A value that specifies whether the workgroup can be accessed from a public network.
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) An array of security group IDs to associate with the workgroup.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) An array of VPC subnet IDs to associate with the workgroup.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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

    """
    The Redshift Workgroup ID.
    """
    workgroup_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the workgroup.
    """
    workgroup_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        namespace_name: str | core.StringOut,
        workgroup_name: str | core.StringOut,
        base_capacity: int | core.IntOut | None = None,
        config_parameter: list[ConfigParameter] | core.ArrayOut[ConfigParameter] | None = None,
        enhanced_vpc_routing: bool | core.BoolOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workgroup.Args(
                namespace_name=namespace_name,
                workgroup_name=workgroup_name,
                base_capacity=base_capacity,
                config_parameter=config_parameter,
                enhanced_vpc_routing=enhanced_vpc_routing,
                publicly_accessible=publicly_accessible,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        base_capacity: int | core.IntOut | None = core.arg(default=None)

        config_parameter: list[ConfigParameter] | core.ArrayOut[ConfigParameter] | None = core.arg(
            default=None
        )

        enhanced_vpc_routing: bool | core.BoolOut | None = core.arg(default=None)

        namespace_name: str | core.StringOut = core.arg()

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        workgroup_name: str | core.StringOut = core.arg()
