import terrascript.core as core


@core.data(type="aws_partition", namespace="meta_data_sources")
class DsPartition(core.Data):
    """
    Base DNS domain name for the current partition (e.g., `amazonaws.com` in AWS Commercial, `amazonaws.
    com.cn` in AWS China).
    """

    dns_suffix: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the current partition (e.g., `aws` in AWS Commercial, `aws-cn` in AWS China).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the current partition (e.g., `aws` in AWS Commercial, `aws-cn` in AWS China).
    """
    partition: str | core.StringOut = core.attr(str, computed=True)

    """
    Prefix of service names (e.g., `com.amazonaws` in AWS Commercial, `cn.com.amazonaws` in AWS China).
    """
    reverse_dns_prefix: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsPartition.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
