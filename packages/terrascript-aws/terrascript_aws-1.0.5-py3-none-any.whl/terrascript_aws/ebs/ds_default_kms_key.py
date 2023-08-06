import terrascript.core as core


@core.data(type="aws_ebs_default_kms_key", namespace="ebs")
class DsDefaultKmsKey(core.Data):
    """
    Region of the default KMS Key.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the default KMS key uses to encrypt an EBS volume in this region when
    no key is specified in an API call that creates the volume and encryption by default is enabled.
    """
    key_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsDefaultKmsKey.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
