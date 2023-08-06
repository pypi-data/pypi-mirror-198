import terrascript.core as core


@core.resource(type="aws_db_instance_role_association", namespace="rds")
class DbInstanceRoleAssociation(core.Resource):
    """
    (Required) DB Instance Identifier to associate with the IAM Role.
    """

    db_instance_identifier: str | core.StringOut = core.attr(str)

    """
    (Required) Name of the feature for association. This can be found in the AWS documentation relevant
    to the integration or a full list is available in the `SupportedFeatureNames` list returned by [AWS
    CLI rds describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-d
    b-engine-versions.html).
    """
    feature_name: str | core.StringOut = core.attr(str)

    """
    DB Instance Identifier and IAM Role ARN separated by a comma (`,`)
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the IAM Role to associate with the DB Instance.
    """
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
