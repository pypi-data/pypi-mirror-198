import terrascript.core as core


@core.resource(type="aws_key_pair", namespace="ec2")
class KeyPair(core.Resource):
    """
    The key pair ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The MD5 public key fingerprint as specified in section 4 of RFC 4716.
    """
    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    """
    The key pair name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name for the key pair. If neither `key_name` nor `key_name_prefix` is provided, Terra
    form will create a unique key name using the prefix `terraform-`.
    """
    key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `key_name`. If
    neither `key_name` nor `key_name_prefix` is provided, Terraform will create a unique key name using
    the prefix `terraform-`.
    """
    key_name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The key pair ID.
    """
    key_pair_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of key pair.
    """
    key_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The public key material.
    """
    public_key: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        public_key: str | core.StringOut,
        key_name: str | core.StringOut | None = None,
        key_name_prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeyPair.Args(
                public_key=public_key,
                key_name=key_name,
                key_name_prefix=key_name_prefix,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_name: str | core.StringOut | None = core.arg(default=None)

        key_name_prefix: str | core.StringOut | None = core.arg(default=None)

        public_key: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
