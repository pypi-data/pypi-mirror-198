import terrascript.core as core


@core.resource(type="aws_ebs_volume", namespace="aws_ebs")
class Volume(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    multi_attach_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: str | core.StringOut,
        encrypted: bool | core.BoolOut | None = None,
        final_snapshot: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        multi_attach_enabled: bool | core.BoolOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
        size: int | core.IntOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        throughput: int | core.IntOut | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Volume.Args(
                availability_zone=availability_zone,
                encrypted=encrypted,
                final_snapshot=final_snapshot,
                iops=iops,
                kms_key_id=kms_key_id,
                multi_attach_enabled=multi_attach_enabled,
                outpost_arn=outpost_arn,
                size=size,
                snapshot_id=snapshot_id,
                tags=tags,
                tags_all=tags_all,
                throughput=throughput,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        multi_attach_enabled: bool | core.BoolOut | None = core.arg(default=None)

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

        size: int | core.IntOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
