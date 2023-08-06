import terrascript.core as core


@core.resource(type="aws_redshift_cluster_iam_roles", namespace="aws_redshift")
class ClusterIamRoles(core.Resource):

    cluster_identifier: str | core.StringOut = core.attr(str)

    default_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    iam_role_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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
