import terrascript.core as core


@core.data(type="aws_ssoadmin_permission_set", namespace="ssoadmin")
class DsPermissionSet(core.Data):
    """
    (Optional) The Amazon Resource Name (ARN) of the permission set.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the Permission Set.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the Permission Set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Resource Name (ARN) of the SSO Instance associated with the permission set.
    """
    instance_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the SSO Permission Set.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The relay state URL used to redirect users within the application during the federation authenticati
    on process.
    """
    relay_state: str | core.StringOut = core.attr(str, computed=True)

    """
    The length of time that the application user sessions are valid in the ISO-8601 standard.
    """
    session_duration: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_arn: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPermissionSet.Args(
                instance_arn=instance_arn,
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        instance_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
