import terrascript.core as core


@core.resource(type="aws_iam_access_key", namespace="iam")
class AccessKey(core.Resource):
    """
    Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the access k
    ey was created.
    """

    create_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Encrypted secret, base64 encoded, if `pgp_key` was specified. This attribute is not available for im
    ported resources. The encrypted secret may be decrypted using the command line, for example: `terraf
    orm output -raw encrypted_secret | base64 --decode | keybase pgp decrypt`.
    """
    encrypted_secret: str | core.StringOut = core.attr(str, computed=True)

    """
    Encrypted SES SMTP password, base64 encoded, if `pgp_key` was specified. This attribute is not avail
    able for imported resources. The encrypted password may be decrypted using the command line, for exa
    mple: `terraform output -raw encrypted_ses_smtp_password_v4 | base64 --decode | keybase pgp decrypt`
    .
    """
    encrypted_ses_smtp_password_v4: str | core.StringOut = core.attr(str, computed=True)

    """
    Access key ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Fingerprint of the PGP key used to encrypt the secret. This attribute is not available for imported
    resources.
    """
    key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_
    person_that_exists`, for use in the `encrypted_secret` output attribute.
    """
    pgp_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    Secret access key. This attribute is not available for imported resources. Note that this will be wr
    itten to the state file. If you use this, please protect your backend state file judiciously. Altern
    atively, you may supply a `pgp_key` instead, which will prevent the secret from being stored in plai
    ntext, at the cost of preventing the use of the secret key in automation.
    """
    secret: str | core.StringOut = core.attr(str, computed=True)

    """
    Secret access key converted into an SES SMTP password by applying [AWS's documented Sigv4 conversion
    algorithm](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html#smtp-credent
    ials-convert). This attribute is not available for imported resources. As SigV4 is region specific,
    valid Provider regions are `ap-south-1`, `ap-southeast-2`, `eu-central-1`, `eu-west-1`, `us-east-1`
    and `us-west-2`. See current [AWS SES regions](https://docs.aws.amazon.com/general/latest/gr/rande.h
    tml#ses_region).
    """
    ses_smtp_password_v4: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Access key status to apply. Defaults to `Active`. Valid values are `Active` and `Inactive
    .
    """
    status: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) IAM user to associate with this access key.
    """
    user: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user: str | core.StringOut,
        pgp_key: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessKey.Args(
                user=user,
                pgp_key=pgp_key,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        pgp_key: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        user: str | core.StringOut = core.arg()
