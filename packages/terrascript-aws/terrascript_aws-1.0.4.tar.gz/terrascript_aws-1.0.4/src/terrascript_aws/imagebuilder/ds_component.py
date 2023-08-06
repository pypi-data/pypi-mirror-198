import terrascript.core as core


@core.data(type="aws_imagebuilder_component", namespace="imagebuilder")
class DsComponent(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the component.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Change description of the component.
    """
    change_description: str | core.StringOut = core.attr(str, computed=True)

    """
    Data of the component.
    """
    data: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the component was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the component.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Encryption status of the component.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the component.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the component.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Owner of the component.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    Platform of the component.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    Operating Systems (OSes) supported by the component.
    """
    supported_os_versions: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Key-value map of resource tags for the component.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Type of the component.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    """
    Version of the component.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsComponent.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
