import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_tag_option_resource_association", namespace="servicecatalog"
)
class TagOptionResourceAssociation(core.Resource):
    """
    Identifier of the association.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the resource.
    """
    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Creation time of the resource.
    """
    resource_created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the resource.
    """
    resource_description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Resource identifier.
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    Description of the resource.
    """
    resource_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Tag Option identifier.
    """
    tag_option_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_id: str | core.StringOut,
        tag_option_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TagOptionResourceAssociation.Args(
                resource_id=resource_id,
                tag_option_id=tag_option_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_id: str | core.StringOut = core.arg()

        tag_option_id: str | core.StringOut = core.arg()
