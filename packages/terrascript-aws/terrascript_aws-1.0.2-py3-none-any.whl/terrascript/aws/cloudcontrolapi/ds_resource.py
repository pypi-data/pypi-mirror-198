import terrascript.core as core


@core.data(type="aws_cloudcontrolapi_resource", namespace="aws_cloudcontrolapi")
class DsResource(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    identifier: str | core.StringOut = core.attr(str)

    properties: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    type_name: str | core.StringOut = core.attr(str)

    type_version_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        identifier: str | core.StringOut,
        type_name: str | core.StringOut,
        role_arn: str | core.StringOut | None = None,
        type_version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResource.Args(
                identifier=identifier,
                type_name=type_name,
                role_arn=role_arn,
                type_version_id=type_version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifier: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut = core.arg()

        type_version_id: str | core.StringOut | None = core.arg(default=None)
