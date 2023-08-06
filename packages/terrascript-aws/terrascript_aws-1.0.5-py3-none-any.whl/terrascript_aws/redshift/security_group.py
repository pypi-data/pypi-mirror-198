import terrascript.core as core


@core.schema
class Ingress(core.Schema):

    cidr: str | core.StringOut | None = core.attr(str, default=None)

    security_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    security_group_owner_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cidr: str | core.StringOut | None = None,
        security_group_name: str | core.StringOut | None = None,
        security_group_owner_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Ingress.Args(
                cidr=cidr,
                security_group_name=security_group_name,
                security_group_owner_id=security_group_owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut | None = core.arg(default=None)

        security_group_name: str | core.StringOut | None = core.arg(default=None)

        security_group_owner_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_redshift_security_group", namespace="redshift")
class SecurityGroup(core.Resource):
    """
    (Optional) The description of the Redshift security group. Defaults to "Managed by Terraform".
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Redshift security group ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of ingress rules.
    """
    ingress: list[Ingress] | core.ArrayOut[Ingress] = core.attr(Ingress, kind=core.Kind.array)

    """
    (Required) The name of the Redshift security group.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ingress: list[Ingress] | core.ArrayOut[Ingress],
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecurityGroup.Args(
                ingress=ingress,
                name=name,
                description=description,
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
