import terrascript.core as core


@core.resource(type="aws_iot_thing_principal_attachment", namespace="aws_iot")
class ThingPrincipalAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    principal: str | core.StringOut = core.attr(str)

    thing: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        principal: str | core.StringOut,
        thing: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingPrincipalAttachment.Args(
                principal=principal,
                thing=thing,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        principal: str | core.StringOut = core.arg()

        thing: str | core.StringOut = core.arg()
