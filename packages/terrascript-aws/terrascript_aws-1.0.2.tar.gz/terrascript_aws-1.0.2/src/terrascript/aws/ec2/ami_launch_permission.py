import terrascript.core as core


@core.resource(type="aws_ami_launch_permission", namespace="aws_ec2")
class AmiLaunchPermission(core.Resource):

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    group: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_id: str | core.StringOut = core.attr(str)

    organization_arn: str | core.StringOut | None = core.attr(str, default=None)

    organizational_unit_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        image_id: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        group: str | core.StringOut | None = None,
        organization_arn: str | core.StringOut | None = None,
        organizational_unit_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AmiLaunchPermission.Args(
                image_id=image_id,
                account_id=account_id,
                group=group,
                organization_arn=organization_arn,
                organizational_unit_arn=organizational_unit_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        group: str | core.StringOut | None = core.arg(default=None)

        image_id: str | core.StringOut = core.arg()

        organization_arn: str | core.StringOut | None = core.arg(default=None)

        organizational_unit_arn: str | core.StringOut | None = core.arg(default=None)
