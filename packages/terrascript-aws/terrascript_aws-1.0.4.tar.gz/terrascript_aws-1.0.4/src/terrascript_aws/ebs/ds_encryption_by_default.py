import terrascript.core as core


@core.data(type="aws_ebs_encryption_by_default", namespace="ebs")
class DsEncryptionByDefault(core.Data):
    """
    Whether or not default EBS encryption is enabled. Returns as `true` or `false`.
    """

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Region of default EBS encryption.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsEncryptionByDefault.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
