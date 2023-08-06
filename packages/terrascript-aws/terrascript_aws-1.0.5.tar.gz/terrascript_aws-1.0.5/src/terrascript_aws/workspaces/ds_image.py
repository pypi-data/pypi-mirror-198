import terrascript.core as core


@core.data(type="aws_workspaces_image", namespace="workspaces")
class DsImage(core.Data):

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str, computed=True)

    operating_system_type: str | core.StringOut = core.attr(str, computed=True)

    required_tenancy: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        image_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsImage.Args(
                image_id=image_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_id: str | core.StringOut = core.arg()
