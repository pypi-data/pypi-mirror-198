import terrascript.core as core


@core.resource(type="aws_volume_attachment", namespace="aws_ebs")
class VolumeAttachment(core.Resource):

    device_name: str | core.StringOut = core.attr(str)

    force_detach: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    skip_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    stop_instance_before_detaching: bool | core.BoolOut | None = core.attr(bool, default=None)

    volume_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        device_name: str | core.StringOut,
        instance_id: str | core.StringOut,
        volume_id: str | core.StringOut,
        force_detach: bool | core.BoolOut | None = None,
        skip_destroy: bool | core.BoolOut | None = None,
        stop_instance_before_detaching: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VolumeAttachment.Args(
                device_name=device_name,
                instance_id=instance_id,
                volume_id=volume_id,
                force_detach=force_detach,
                skip_destroy=skip_destroy,
                stop_instance_before_detaching=stop_instance_before_detaching,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_name: str | core.StringOut = core.arg()

        force_detach: bool | core.BoolOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        skip_destroy: bool | core.BoolOut | None = core.arg(default=None)

        stop_instance_before_detaching: bool | core.BoolOut | None = core.arg(default=None)

        volume_id: str | core.StringOut = core.arg()
