import terrascript.core as core


@core.schema
class CidrAuthorizationContext(core.Schema):

    message: str | core.StringOut | None = core.attr(str, default=None)

    signature: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: str | core.StringOut | None = None,
        signature: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CidrAuthorizationContext.Args(
                message=message,
                signature=signature,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: str | core.StringOut | None = core.arg(default=None)

        signature: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_vpc_ipam_pool_cidr", namespace="vpc_ipam")
class PoolCidr(core.Resource):

    cidr: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cidr_authorization_context: CidrAuthorizationContext | None = core.attr(
        CidrAuthorizationContext, default=None
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    ipam_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ipam_pool_id: str | core.StringOut,
        cidr: str | core.StringOut | None = None,
        cidr_authorization_context: CidrAuthorizationContext | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolCidr.Args(
                ipam_pool_id=ipam_pool_id,
                cidr=cidr,
                cidr_authorization_context=cidr_authorization_context,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr: str | core.StringOut | None = core.arg(default=None)

        cidr_authorization_context: CidrAuthorizationContext | None = core.arg(default=None)

        ipam_pool_id: str | core.StringOut = core.arg()
