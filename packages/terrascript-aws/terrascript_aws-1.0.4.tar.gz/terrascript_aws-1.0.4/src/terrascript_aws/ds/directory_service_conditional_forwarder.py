import terrascript.core as core


@core.resource(type="aws_directory_service_conditional_forwarder", namespace="ds")
class DirectoryServiceConditionalForwarder(core.Resource):
    """
    (Required) The id of directory.
    """

    directory_id: str | core.StringOut = core.attr(str)

    """
    (Required) A list of forwarder IP addresses.
    """
    dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The fully qualified domain name of the remote domain for which forwarders will be used.
    """
    remote_domain_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: str | core.StringOut,
        dns_ips: list[str] | core.ArrayOut[core.StringOut],
        remote_domain_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceConditionalForwarder.Args(
                directory_id=directory_id,
                dns_ips=dns_ips,
                remote_domain_name=remote_domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: str | core.StringOut = core.arg()

        dns_ips: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        remote_domain_name: str | core.StringOut = core.arg()
