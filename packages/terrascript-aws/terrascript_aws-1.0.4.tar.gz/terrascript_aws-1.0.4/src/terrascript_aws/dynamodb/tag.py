import terrascript.core as core


@core.resource(type="aws_dynamodb_tag", namespace="dynamodb")
class Tag(core.Resource):
    """
    DynamoDB resource identifier and key, separated by a comma (`,`)
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Tag name.
    """
    key: str | core.StringOut = core.attr(str)

    """
    (Required) Amazon Resource Name (ARN) of the DynamoDB resource to tag.
    """
    resource_arn: str | core.StringOut = core.attr(str)

    """
    (Required) Tag value.
    """
    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key: str | core.StringOut,
        resource_arn: str | core.StringOut,
        value: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Tag.Args(
                key=key,
                resource_arn=resource_arn,
                value=value,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()
