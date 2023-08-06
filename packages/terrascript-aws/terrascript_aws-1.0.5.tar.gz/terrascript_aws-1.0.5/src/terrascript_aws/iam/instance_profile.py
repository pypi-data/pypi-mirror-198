import terrascript.core as core


@core.resource(type="aws_iam_instance_profile", namespace="iam")
class InstanceProfile(core.Resource):
    """
    ARN assigned by AWS to the instance profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Creation timestamp of the instance profile.
    """
    create_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Instance profile's ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) Name of the instance profile. If omitted, Terraform will assign a ra
    ndom, unique name. Conflicts with `name_prefix`. Can be a string of characters consisting of upper a
    nd lowercase alphanumeric characters and these special characters: `_`, `+`, `=`, `,`, `.`, `@`, `-`
    . Spaces are not allowed.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, default "/") Path to the instance profile. For more information about paths, see [IAM Ide
    ntifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the IAM User G
    uide. Can be a string of characters consisting of either a forward slash (`/`) by itself or a string
    that must begin and end with forward slashes. Can include any ASCII character from the ! (\u0021) t
    hrough the DEL character (\u007F), including most punctuation characters, digits, and upper and lowe
    rcase letters.
    """
    path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the role to add to the profile.
    """
    role: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of resource tags for the IAM Instance Profile. If configured with a provider [`defaul
    t_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defau
    lt_tags-configuration-block) present, tags with matching keys will overwrite those defined at the pr
    ovider-level.
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

    """
    [Unique ID][1] assigned by AWS.
    """
    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
        role: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceProfile.Args(
                name=name,
                name_prefix=name_prefix,
                path=path,
                role=role,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)

        role: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
