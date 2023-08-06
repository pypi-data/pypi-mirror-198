import terrascript.core as core


@core.resource(type="aws_ssm_activation", namespace="ssm")
class Activation(core.Resource):
    """
    The code the system generates when it processes the activation.
    """

    activation_code: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the resource that you want to register.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) UTC timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by whi
    ch this activation request should expire. The default value is 24 hours from resource creation time.
    Terraform will only perform drift detection of its value when present in a configuration.
    """
    expiration_date: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    If the current activation has expired.
    """
    expired: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) The IAM Role to attach to the managed instance.
    """
    iam_role: str | core.StringOut = core.attr(str)

    """
    The activation ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The default name of the registered managed instance.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The number of managed instances that are currently registered using this activation.
    """
    registration_count: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) The maximum number of managed instances you want to register. The default value is 1 inst
    ance.
    """
    registration_limit: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A map of tags to assign to the object. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
        iam_role: str | core.StringOut,
        description: str | core.StringOut | None = None,
        expiration_date: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        registration_limit: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Activation.Args(
                iam_role=iam_role,
                description=description,
                expiration_date=expiration_date,
                name=name,
                registration_limit=registration_limit,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        expiration_date: str | core.StringOut | None = core.arg(default=None)

        iam_role: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        registration_limit: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
