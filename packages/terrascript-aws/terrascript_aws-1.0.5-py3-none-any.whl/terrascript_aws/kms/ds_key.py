import terrascript.core as core


@core.schema
class PrimaryKey(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        region: str | core.StringOut,
    ):
        super().__init__(
            args=PrimaryKey.Args(
                arn=arn,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        region: str | core.StringOut = core.arg()


@core.schema
class ReplicaKeys(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        region: str | core.StringOut,
    ):
        super().__init__(
            args=ReplicaKeys.Args(
                arn=arn,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        region: str | core.StringOut = core.arg()


@core.schema
class MultiRegionConfiguration(core.Schema):

    multi_region_key_type: str | core.StringOut = core.attr(str, computed=True)

    primary_key: list[PrimaryKey] | core.ArrayOut[PrimaryKey] = core.attr(
        PrimaryKey, computed=True, kind=core.Kind.array
    )

    replica_keys: list[ReplicaKeys] | core.ArrayOut[ReplicaKeys] = core.attr(
        ReplicaKeys, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        multi_region_key_type: str | core.StringOut,
        primary_key: list[PrimaryKey] | core.ArrayOut[PrimaryKey],
        replica_keys: list[ReplicaKeys] | core.ArrayOut[ReplicaKeys],
    ):
        super().__init__(
            args=MultiRegionConfiguration.Args(
                multi_region_key_type=multi_region_key_type,
                primary_key=primary_key,
                replica_keys=replica_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        multi_region_key_type: str | core.StringOut = core.arg()

        primary_key: list[PrimaryKey] | core.ArrayOut[PrimaryKey] = core.arg()

        replica_keys: list[ReplicaKeys] | core.ArrayOut[ReplicaKeys] = core.arg()


@core.data(type="aws_kms_key", namespace="kms")
class DsKey(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_account_id: str | core.StringOut = core.attr(str, computed=True)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    customer_master_key_spec: str | core.StringOut = core.attr(str, computed=True)

    deletion_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    expiration_model: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of grant tokens
    """
    grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Key identifier which can be one of the following format:
    """
    key_id: str | core.StringOut = core.attr(str)

    key_manager: str | core.StringOut = core.attr(str, computed=True)

    key_state: str | core.StringOut = core.attr(str, computed=True)

    key_usage: str | core.StringOut = core.attr(str, computed=True)

    multi_region: bool | core.BoolOut = core.attr(bool, computed=True)

    multi_region_configuration: list[MultiRegionConfiguration] | core.ArrayOut[
        MultiRegionConfiguration
    ] = core.attr(MultiRegionConfiguration, computed=True, kind=core.Kind.array)

    origin: str | core.StringOut = core.attr(str, computed=True)

    valid_to: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        key_id: str | core.StringOut,
        grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsKey.Args(
                key_id=key_id,
                grant_tokens=grant_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        key_id: str | core.StringOut = core.arg()
