import terrascript.core as core


@core.resource(type="aws_account_alternate_contact", namespace="account")
class AlternateContact(core.Resource):
    """
    (Optional) The ID of the target account when managing member accounts. Will manage current user's ac
    count by default if omitted.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY
    .
    """
    alternate_contact_type: str | core.StringOut = core.attr(str)

    """
    (Required) An email address for the alternate contact.
    """
    email_address: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the alternate contact.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A phone number for the alternate contact.
    """
    phone_number: str | core.StringOut = core.attr(str)

    """
    (Required) A title for the alternate contact.
    """
    title: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        alternate_contact_type: str | core.StringOut,
        email_address: str | core.StringOut,
        name: str | core.StringOut,
        phone_number: str | core.StringOut,
        title: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AlternateContact.Args(
                alternate_contact_type=alternate_contact_type,
                email_address=email_address,
                name=name,
                phone_number=phone_number,
                title=title,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        alternate_contact_type: str | core.StringOut = core.arg()

        email_address: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        phone_number: str | core.StringOut = core.arg()

        title: str | core.StringOut = core.arg()
