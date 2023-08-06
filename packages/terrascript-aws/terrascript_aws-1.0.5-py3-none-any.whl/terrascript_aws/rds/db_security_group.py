import terrascript.core as core


@core.schema
class Ingress(core.Schema):

    cidr: str | core.StringOut | None = core.attr(str, default=None)

    security_group_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    security_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    security_group_owner_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cidr: str | core.StringOut | None = None,
        security_group_id: str | core.StringOut | None = None,
        security_group_name: str | core.StringOut | None = None,
        security_group_owner_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Ingress.Args(
                cidr=cidr,
                security_group_id=security_group_id,
                security_group_name=security_group_name,
                security_group_owner_id=security_group_owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut | None = core.arg(default=None)

        security_group_id: str | core.StringOut | None = core.arg(default=None)

        security_group_name: str | core.StringOut | None = core.arg(default=None)

        security_group_owner_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_db_security_group", namespace="rds")
class DbSecurityGroup(core.Resource):
    """
    The arn of the DB security group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the DB security group. Defaults to "Managed by Terraform".
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The db security group ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of ingress rules.
    """
    ingress: list[Ingress] | core.ArrayOut[Ingress] = core.attr(Ingress, kind=core.Kind.array)

    """
    (Required) The name of the DB security group.
    """
    name: str | core.StringOut = core.attr(str)

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

    def __init__(
        self,
        resource_name: str,
        *,
        ingress: list[Ingress] | core.ArrayOut[Ingress],
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSecurityGroup.Args(
                ingress=ingress,
                name=name,
                description=description,
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

        ingress: list[Ingress] | core.ArrayOut[Ingress] = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
