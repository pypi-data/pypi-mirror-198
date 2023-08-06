import terrascript.core as core


@core.resource(type="aws_db_instance_role_association", namespace="aws_rds")
class DbInstanceRoleAssociation(core.Resource):

    db_instance_identifier: str | core.StringOut = core.attr(str)

    feature_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        db_instance_identifier: str | core.StringOut,
        feature_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbInstanceRoleAssociation.Args(
                db_instance_identifier=db_instance_identifier,
                feature_name=feature_name,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_instance_identifier: str | core.StringOut = core.arg()

        feature_name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()
