import terrascript.core as core


@core.resource(type="aws_elb_attachment", namespace="elb")
class Attachment(core.Resource):
    """
    (Required) The name of the ELB.
    """

    elb: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Instance ID to place in the ELB pool.
    """
    instance: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        elb: str | core.StringOut,
        instance: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Attachment.Args(
                elb=elb,
                instance=instance,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        elb: str | core.StringOut = core.arg()

        instance: str | core.StringOut = core.arg()
