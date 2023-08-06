import terrascript.core as core


@core.resource(type="aws_iam_user", namespace="iam")
class User(core.Resource):
    """
    The ARN assigned by AWS for this user.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, default false) When destroying this user, destroy even if it
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The user's name. The name must consist of upper and lowercase alphanumeric characters wit
    h no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not dis
    tinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional, default "/") Path in which to create the user.
    """
    path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the policy that is used to set the permissions boundary for the user.
    """
    permissions_boundary: str | core.StringOut | None = core.attr(str, default=None)

    """
    Key-value map of tags for the IAM user. If configured with a provider [`default_tags` configuration
    block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-
    block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    The [unique ID][1] assigned by AWS.
    """
    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        force_destroy: bool | core.BoolOut | None = None,
        path: str | core.StringOut | None = None,
        permissions_boundary: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                name=name,
                force_destroy=force_destroy,
                path=path,
                permissions_boundary=permissions_boundary,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        path: str | core.StringOut | None = core.arg(default=None)

        permissions_boundary: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
