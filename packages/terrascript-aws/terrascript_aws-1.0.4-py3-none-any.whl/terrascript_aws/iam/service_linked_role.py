import terrascript.core as core


@core.resource(type="aws_iam_service_linked_role", namespace="iam")
class ServiceLinkedRole(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the role.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The AWS service to which this role is attached. You use a string sim
    ilar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To
    find the full list of services that support service-linked roles, check [the docs](https://docs.aws.
    amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
    """
    aws_service_name: str | core.StringOut = core.attr(str)

    """
    The creation date of the IAM role.
    """
    create_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, forces new resource) Additional string appended to the role name. Not all AWS services su
    pport custom suffixes.
    """
    custom_suffix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The description of the role.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) of the role.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the role.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    The path of the role.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value mapping of tags for the IAM role. If configured with a provider [`default_tags` configurat
    ion block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurat
    ion-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    The stable and unique string identifying the role.
    """
    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        aws_service_name: str | core.StringOut,
        custom_suffix: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceLinkedRole.Args(
                aws_service_name=aws_service_name,
                custom_suffix=custom_suffix,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_service_name: str | core.StringOut = core.arg()

        custom_suffix: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
