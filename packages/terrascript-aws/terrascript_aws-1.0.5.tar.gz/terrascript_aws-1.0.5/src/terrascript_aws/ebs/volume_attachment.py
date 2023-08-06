import terrascript.core as core


@core.resource(type="aws_volume_attachment", namespace="ebs")
class VolumeAttachment(core.Resource):
    """
    (Required) The device name to expose to the instance (for
    """

    device_name: str | core.StringOut = core.attr(str)

    """
    (Optional, Boolean) Set to `true` if you want to force the
    """
    force_detach: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the Instance to attach to
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Optional, Boolean) Set this to true if you do not wish
    """
    skip_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Boolean) Set this to true to ensure that the target instance is stopped
    """
    stop_instance_before_detaching: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) ID of the Volume to be attached
    """
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
