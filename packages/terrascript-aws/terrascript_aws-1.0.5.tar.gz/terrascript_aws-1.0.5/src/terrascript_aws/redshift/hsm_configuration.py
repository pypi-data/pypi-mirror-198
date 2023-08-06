import terrascript.core as core


@core.resource(type="aws_redshift_hsm_configuration", namespace="redshift")
class HsmConfiguration(core.Resource):
    """
    Amazon Resource Name (ARN) of the Hsm Client Certificate.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) A text description of the HSM configuration to be created.
    """
    description: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The identifier to be assigned to the new Amazon Redshift HSM configu
    ration.
    """
    hsm_configuration_identifier: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The IP address that the Amazon Redshift cluster must use to access t
    he HSM.
    """
    hsm_ip_address: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The name of the partition in the HSM where the Amazon Redshift clust
    ers will store their database encryption keys.
    """
    hsm_partition_name: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The password required to access the HSM partition.
    """
    hsm_partition_password: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The HSMs public certificate file. When using Cloud HSM, the file nam
    e is server.pem.
    """
    hsm_server_public_certificate: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut,
        hsm_configuration_identifier: str | core.StringOut,
        hsm_ip_address: str | core.StringOut,
        hsm_partition_name: str | core.StringOut,
        hsm_partition_password: str | core.StringOut,
        hsm_server_public_certificate: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HsmConfiguration.Args(
                description=description,
                hsm_configuration_identifier=hsm_configuration_identifier,
                hsm_ip_address=hsm_ip_address,
                hsm_partition_name=hsm_partition_name,
                hsm_partition_password=hsm_partition_password,
                hsm_server_public_certificate=hsm_server_public_certificate,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut = core.arg()

        hsm_configuration_identifier: str | core.StringOut = core.arg()

        hsm_ip_address: str | core.StringOut = core.arg()

        hsm_partition_name: str | core.StringOut = core.arg()

        hsm_partition_password: str | core.StringOut = core.arg()

        hsm_server_public_certificate: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
