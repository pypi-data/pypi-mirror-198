import terrascript.core as core


@core.data(type="aws_ec2_serial_console_access", namespace="ec2")
class DsSerialConsoleAccess(core.Data):
    """
    Whether or not serial console access is enabled. Returns as `true` or `false`.
    """

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Region of serial console access.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsSerialConsoleAccess.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
