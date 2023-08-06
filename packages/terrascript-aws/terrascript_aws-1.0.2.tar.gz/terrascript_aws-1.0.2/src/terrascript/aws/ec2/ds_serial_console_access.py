import terrascript.core as core


@core.data(type="aws_ec2_serial_console_access", namespace="aws_ec2")
class DsSerialConsoleAccess(core.Data):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

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
