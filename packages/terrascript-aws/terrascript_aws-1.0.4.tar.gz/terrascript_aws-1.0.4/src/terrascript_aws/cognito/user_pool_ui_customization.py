import terrascript.core as core


@core.resource(type="aws_cognito_user_pool_ui_customization", namespace="cognito")
class UserPoolUiCustomization(core.Resource):

    client_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The creation date in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) for the UI cu
    stomization.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    css: str | core.StringOut | None = core.attr(str, default=None)

    """
    The CSS version number.
    """
    css_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_file: str | core.StringOut | None = core.attr(str, default=None)

    """
    The logo image URL for the UI customization.
    """
    image_url: str | core.StringOut = core.attr(str, computed=True)

    """
    The last-modified date in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) for the
    UI customization.
    """
    last_modified_date: str | core.StringOut = core.attr(str, computed=True)

    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_pool_id: str | core.StringOut,
        client_id: str | core.StringOut | None = None,
        css: str | core.StringOut | None = None,
        image_file: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPoolUiCustomization.Args(
                user_pool_id=user_pool_id,
                client_id=client_id,
                css=css,
                image_file=image_file,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_id: str | core.StringOut | None = core.arg(default=None)

        css: str | core.StringOut | None = core.arg(default=None)

        image_file: str | core.StringOut | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()
