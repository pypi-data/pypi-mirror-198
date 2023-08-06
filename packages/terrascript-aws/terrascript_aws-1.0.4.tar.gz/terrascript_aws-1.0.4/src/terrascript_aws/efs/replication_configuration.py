import terrascript.core as core


@core.schema
class Destination(core.Schema):

    availability_zone_name: str | core.StringOut | None = core.attr(str, default=None)

    file_system_id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        file_system_id: str | core.StringOut,
        status: str | core.StringOut,
        availability_zone_name: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Destination.Args(
                file_system_id=file_system_id,
                status=status,
                availability_zone_name=availability_zone_name,
                kms_key_id=kms_key_id,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_name: str | core.StringOut | None = core.arg(default=None)

        file_system_id: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()


@core.resource(type="aws_efs_replication_configuration", namespace="efs")
class ReplicationConfiguration(core.Resource):
    """
    When the replication configuration was created.
    """

    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A destination configuration block (documented below).
    """
    destination: Destination = core.attr(Destination)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the original source Amazon EFS file system in the replication conf
    iguration.
    """
    original_source_file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the current source file system in the replication configuration.
    """
    source_file_system_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the file system that is to be replicated.
    """
    source_file_system_id: str | core.StringOut = core.attr(str)

    """
    The AWS Region in which the source Amazon EFS file system is located.
    """
    source_file_system_region: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination: Destination,
        source_file_system_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationConfiguration.Args(
                destination=destination,
                source_file_system_id=source_file_system_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: Destination = core.arg()

        source_file_system_id: str | core.StringOut = core.arg()
