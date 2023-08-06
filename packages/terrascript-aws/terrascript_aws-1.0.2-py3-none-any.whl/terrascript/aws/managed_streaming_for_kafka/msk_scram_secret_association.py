import terrascript.core as core


@core.resource(type="aws_msk_scram_secret_association", namespace="aws_managed_streaming_for_kafka")
class MskScramSecretAssociation(core.Resource):

    cluster_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    secret_arn_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_arn: str | core.StringOut,
        secret_arn_list: list[str] | core.ArrayOut[core.StringOut],
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskScramSecretAssociation.Args(
                cluster_arn=cluster_arn,
                secret_arn_list=secret_arn_list,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_arn: str | core.StringOut = core.arg()

        secret_arn_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()
