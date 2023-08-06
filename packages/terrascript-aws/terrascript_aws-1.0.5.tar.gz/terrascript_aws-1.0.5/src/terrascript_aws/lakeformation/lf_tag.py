import terrascript.core as core


@core.resource(type="aws_lakeformation_lf_tag", namespace="lakeformation")
class LfTag(core.Resource):
    """
    (Optional) ID of the Data Catalog to create the tag in. If omitted, this defaults to the AWS Account
    ID.
    """

    catalog_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Catalog ID and key-name of the tag
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Key-name for the tag.
    """
    key: str | core.StringOut = core.attr(str)

    """
    (Required) List of possible values an attribute can take.
    """
    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
        catalog_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LfTag.Args(
                key=key,
                values=values,
                catalog_id=catalog_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()
