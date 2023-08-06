import terrascript.core as core


@core.resource(type="aws_ec2_tag", namespace="ec2")
class Tag(core.Resource):
    """
    EC2 resource identifier and key, separated by a comma (`,`)
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The tag name.
    """
    key: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the EC2 resource to manage the tag for.
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    (Required) The value of the tag.
    """
    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key: str | core.StringOut,
        resource_id: str | core.StringOut,
        value: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Tag.Args(
                key=key,
                resource_id=resource_id,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()
