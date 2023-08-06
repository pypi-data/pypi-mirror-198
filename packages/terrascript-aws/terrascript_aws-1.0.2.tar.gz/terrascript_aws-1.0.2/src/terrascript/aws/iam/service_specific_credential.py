import terrascript.core as core


@core.resource(type="aws_iam_service_specific_credential", namespace="aws_iam")
class ServiceSpecificCredential(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    service_name: str | core.StringOut = core.attr(str)

    service_password: str | core.StringOut = core.attr(str, computed=True)

    service_specific_credential_id: str | core.StringOut = core.attr(str, computed=True)

    service_user_name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut | None = core.attr(str, default=None)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        service_name: str | core.StringOut,
        user_name: str | core.StringOut,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceSpecificCredential.Args(
                service_name=service_name,
                user_name=user_name,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        service_name: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
