import terrascript.core as core


@core.resource(type="aws_dms_replication_subnet_group", namespace="dms")
class ReplicationSubnetGroup(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    replication_subnet_group_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The description for the subnet group.
    """
    replication_subnet_group_description: str | core.StringOut = core.attr(str)

    """
    (Required) The name for the replication subnet group. This value is stored as a lowercase string.
    """
    replication_subnet_group_id: str | core.StringOut = core.attr(str)

    """
    (Required) A list of the EC2 subnet IDs for the subnet group.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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
    The ID of the VPC the subnet group is in.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        replication_subnet_group_description: str | core.StringOut,
        replication_subnet_group_id: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationSubnetGroup.Args(
                replication_subnet_group_description=replication_subnet_group_description,
                replication_subnet_group_id=replication_subnet_group_id,
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
        replication_subnet_group_description: str | core.StringOut = core.arg()

        replication_subnet_group_id: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
