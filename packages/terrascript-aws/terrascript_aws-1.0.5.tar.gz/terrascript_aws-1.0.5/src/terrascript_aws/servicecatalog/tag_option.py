import terrascript.core as core


@core.resource(type="aws_servicecatalog_tag_option", namespace="servicecatalog")
class TagOption(core.Resource):
    """
    (Optional) Whether tag option is active. Default is `true`.
    """

    active: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Identifier (e.g., `tag-pjtvagohlyo3m`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Tag option key.
    """
    key: str | core.StringOut = core.attr(str)

    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Tag option value.
    """
    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
        active: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TagOption.Args(
                key=key,
                value=value,
                active=active,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active: bool | core.BoolOut | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()
