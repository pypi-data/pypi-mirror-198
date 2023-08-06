import terrascript.core as core


@core.resource(type="aws_opsworks_rds_db_instance", namespace="opsworks")
class RdsDbInstance(core.Resource):
    """
    (Required) A db password
    """

    db_password: str | core.StringOut = core.attr(str)

    """
    (Required) A db username
    """
    db_user: str | core.StringOut = core.attr(str)

    """
    The computed id. Please note that this is only used internally to identify the stack <-> instance re
    lation. This value is not used in aws.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The db instance to register for this stack. Changing this will force a new resource.
    """
    rds_db_instance_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The stack to register a db instance for. Changing this will force a new resource.
    """
    stack_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        db_password: str | core.StringOut,
        db_user: str | core.StringOut,
        rds_db_instance_arn: str | core.StringOut,
        stack_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RdsDbInstance.Args(
                db_password=db_password,
                db_user=db_user,
                rds_db_instance_arn=rds_db_instance_arn,
                stack_id=stack_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_password: str | core.StringOut = core.arg()

        db_user: str | core.StringOut = core.arg()

        rds_db_instance_arn: str | core.StringOut = core.arg()

        stack_id: str | core.StringOut = core.arg()
