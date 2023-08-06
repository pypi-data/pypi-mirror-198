import terrascript.core as core


@core.resource(type="aws_efs_file_system_policy", namespace="aws_efs")
class FileSystemPolicy(core.Resource):

    bypass_policy_lockout_safety_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    file_system_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
