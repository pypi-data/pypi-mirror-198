import terrascript.core as core


@core.resource(type="aws_efs_file_system_policy", namespace="efs")
class FileSystemPolicy(core.Resource):
    """
    (Optional) A flag to indicate whether to bypass the `aws_efs_file_system_policy` lockout safety chec
    k. The policy lockout safety check determines whether the policy in the request will prevent the pri
    ncipal making the request will be locked out from making future `PutFileSystemPolicy` requests on th
    e file system. Set `bypass_policy_lockout_safety_check` to `true` only when you intend to prevent th
    e principal that is making the request from making a subsequent `PutFileSystemPolicy` request on the
    file system. The default value is `false`.
    """

    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The ID of the EFS file system.
    """
    file_system_id: str | core.StringOut = core.attr(str)

    """
    The ID that identifies the file system (e.g., fs-ccfc0d65).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The JSON formatted file system policy for the EFS file system. see [Docs](https://docs.aw
    s.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-
    policies) for more info.
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: str | core.StringOut,
        policy: str | core.StringOut,
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FileSystemPolicy.Args(
                file_system_id=file_system_id,
                policy=policy,
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.arg(default=None)

        file_system_id: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
