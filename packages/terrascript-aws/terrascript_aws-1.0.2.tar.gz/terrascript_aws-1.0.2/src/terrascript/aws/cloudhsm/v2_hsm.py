import terrascript.core as core


@core.resource(type="aws_cloudhsm_v2_hsm", namespace="aws_cloudhsm")
class V2Hsm(core.Resource):

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_id: str | core.StringOut = core.attr(str)

    hsm_eni_id: str | core.StringOut = core.attr(str, computed=True)

    hsm_id: str | core.StringOut = core.attr(str, computed=True)

    hsm_state: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: str | core.StringOut,
        availability_zone: str | core.StringOut | None = None,
        ip_address: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2Hsm.Args(
                cluster_id=cluster_id,
                availability_zone=availability_zone,
                ip_address=ip_address,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        cluster_id: str | core.StringOut = core.arg()

        ip_address: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)
