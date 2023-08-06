import terrascript.core as core


@core.resource(type="aws_redshift_cluster_iam_roles", namespace="redshift")
class ClusterIamRoles(core.Resource):
    """
    (Required) The name of the Redshift Cluster IAM Roles.
    """

    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    (Optional) The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster w
    hen the cluster was created.
    """
    default_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated
    to the cluster at any time.
    """
    iam_role_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The Redshift Cluster ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        default_iam_role_arn: str | core.StringOut | None = None,
        iam_role_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterIamRoles.Args(
                cluster_identifier=cluster_identifier,
                default_iam_role_arn=default_iam_role_arn,
                iam_role_arns=iam_role_arns,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: str | core.StringOut = core.arg()

        default_iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        iam_role_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
