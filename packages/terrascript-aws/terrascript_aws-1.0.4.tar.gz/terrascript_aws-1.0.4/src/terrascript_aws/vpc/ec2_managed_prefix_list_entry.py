import terrascript.core as core


@core.resource(type="aws_ec2_managed_prefix_list_entry", namespace="vpc")
class Ec2ManagedPrefixListEntry(core.Resource):
    """
    (Required) CIDR block of this entry.
    """

    cidr: str | core.StringOut = core.attr(str)

    """
    (Optional) Description of this entry. Due to API limitations, updating only the description of an en
    try requires recreating the entry.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    ID of the managed prefix list entry.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) CIDR block of this entry.
    """
    prefix_list_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cidr: str | core.StringOut,
        prefix_list_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ManagedPrefixListEntry.Args(
                cidr=cidr,
                prefix_list_id=prefix_list_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        prefix_list_id: str | core.StringOut = core.arg()
