import terrascript.core as core


@core.schema
class WorkmailAction(core.Schema):

    organization_arn: str | core.StringOut = core.attr(str)

    position: int | core.IntOut = core.attr(int)

    topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        organization_arn: str | core.StringOut,
        position: int | core.IntOut,
        topic_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=WorkmailAction.Args(
                organization_arn=organization_arn,
                position=position,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        organization_arn: str | core.StringOut = core.arg()

        position: int | core.IntOut = core.arg()

        topic_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AddHeaderAction(core.Schema):

    header_name: str | core.StringOut = core.attr(str)

    header_value: str | core.StringOut = core.attr(str)

    position: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        header_name: str | core.StringOut,
        header_value: str | core.StringOut,
        position: int | core.IntOut,
    ):
        super().__init__(
            args=AddHeaderAction.Args(
                header_name=header_name,
                header_value=header_value,
                position=position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_name: str | core.StringOut = core.arg()

        header_value: str | core.StringOut = core.arg()

        position: int | core.IntOut = core.arg()


@core.schema
class S3Action(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    object_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    position: int | core.IntOut = core.attr(int)

    topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        position: int | core.IntOut,
        kms_key_arn: str | core.StringOut | None = None,
        object_key_prefix: str | core.StringOut | None = None,
        topic_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3Action.Args(
                bucket_name=bucket_name,
                position=position,
                kms_key_arn=kms_key_arn,
                object_key_prefix=object_key_prefix,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        object_key_prefix: str | core.StringOut | None = core.arg(default=None)

        position: int | core.IntOut = core.arg()

        topic_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SnsAction(core.Schema):

    encoding: str | core.StringOut | None = core.attr(str, default=None)

    position: int | core.IntOut = core.attr(int)

    topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        position: int | core.IntOut,
        topic_arn: str | core.StringOut,
        encoding: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SnsAction.Args(
                position=position,
                topic_arn=topic_arn,
                encoding=encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encoding: str | core.StringOut | None = core.arg(default=None)

        position: int | core.IntOut = core.arg()

        topic_arn: str | core.StringOut = core.arg()


@core.schema
class BounceAction(core.Schema):

    message: str | core.StringOut = core.attr(str)

    position: int | core.IntOut = core.attr(int)

    sender: str | core.StringOut = core.attr(str)

    smtp_reply_code: str | core.StringOut = core.attr(str)

    status_code: str | core.StringOut | None = core.attr(str, default=None)

    topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: str | core.StringOut,
        position: int | core.IntOut,
        sender: str | core.StringOut,
        smtp_reply_code: str | core.StringOut,
        status_code: str | core.StringOut | None = None,
        topic_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=BounceAction.Args(
                message=message,
                position=position,
                sender=sender,
                smtp_reply_code=smtp_reply_code,
                status_code=status_code,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: str | core.StringOut = core.arg()

        position: int | core.IntOut = core.arg()

        sender: str | core.StringOut = core.arg()

        smtp_reply_code: str | core.StringOut = core.arg()

        status_code: str | core.StringOut | None = core.arg(default=None)

        topic_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LambdaAction(core.Schema):

    function_arn: str | core.StringOut = core.attr(str)

    invocation_type: str | core.StringOut | None = core.attr(str, default=None)

    position: int | core.IntOut = core.attr(int)

    topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        function_arn: str | core.StringOut,
        position: int | core.IntOut,
        invocation_type: str | core.StringOut | None = None,
        topic_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LambdaAction.Args(
                function_arn=function_arn,
                position=position,
                invocation_type=invocation_type,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: str | core.StringOut = core.arg()

        invocation_type: str | core.StringOut | None = core.arg(default=None)

        position: int | core.IntOut = core.arg()

        topic_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class StopAction(core.Schema):

    position: int | core.IntOut = core.attr(int)

    scope: str | core.StringOut = core.attr(str)

    topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        position: int | core.IntOut,
        scope: str | core.StringOut,
        topic_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=StopAction.Args(
                position=position,
                scope=scope,
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        position: int | core.IntOut = core.arg()

        scope: str | core.StringOut = core.arg()

        topic_arn: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ses_receipt_rule", namespace="ses")
class ReceiptRule(core.Resource):
    """
    (Optional) A list of Add Header Action blocks. Documented below.
    """

    add_header_action: list[AddHeaderAction] | core.ArrayOut[AddHeaderAction] | None = core.attr(
        AddHeaderAction, default=None, kind=core.Kind.array
    )

    """
    (Optional) The name of the rule to place this rule after
    """
    after: str | core.StringOut | None = core.attr(str, default=None)

    """
    The SES receipt rule ARN.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of Bounce Action blocks. Documented below.
    """
    bounce_action: list[BounceAction] | core.ArrayOut[BounceAction] | None = core.attr(
        BounceAction, default=None, kind=core.Kind.array
    )

    """
    (Optional) If true, the rule will be enabled
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The SES receipt rule name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of Lambda Action blocks. Documented below.
    """
    lambda_action: list[LambdaAction] | core.ArrayOut[LambdaAction] | None = core.attr(
        LambdaAction, default=None, kind=core.Kind.array
    )

    """
    (Required) The name of the rule
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of email addresses
    """
    recipients: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The name of the rule set
    """
    rule_set_name: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of S3 Action blocks. Documented below.
    """
    s3_action: list[S3Action] | core.ArrayOut[S3Action] | None = core.attr(
        S3Action, default=None, kind=core.Kind.array
    )

    """
    (Optional) If true, incoming emails will be scanned for spam and viruses
    """
    scan_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A list of SNS Action blocks. Documented below.
    """
    sns_action: list[SnsAction] | core.ArrayOut[SnsAction] | None = core.attr(
        SnsAction, default=None, kind=core.Kind.array
    )

    """
    (Optional) A list of Stop Action blocks. Documented below.
    """
    stop_action: list[StopAction] | core.ArrayOut[StopAction] | None = core.attr(
        StopAction, default=None, kind=core.Kind.array
    )

    """
    (Optional) `Require` or `Optional`
    """
    tls_policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of WorkMail Action blocks. Documented below.
    """
    workmail_action: list[WorkmailAction] | core.ArrayOut[WorkmailAction] | None = core.attr(
        WorkmailAction, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        rule_set_name: str | core.StringOut,
        add_header_action: list[AddHeaderAction] | core.ArrayOut[AddHeaderAction] | None = None,
        after: str | core.StringOut | None = None,
        bounce_action: list[BounceAction] | core.ArrayOut[BounceAction] | None = None,
        enabled: bool | core.BoolOut | None = None,
        lambda_action: list[LambdaAction] | core.ArrayOut[LambdaAction] | None = None,
        recipients: list[str] | core.ArrayOut[core.StringOut] | None = None,
        s3_action: list[S3Action] | core.ArrayOut[S3Action] | None = None,
        scan_enabled: bool | core.BoolOut | None = None,
        sns_action: list[SnsAction] | core.ArrayOut[SnsAction] | None = None,
        stop_action: list[StopAction] | core.ArrayOut[StopAction] | None = None,
        tls_policy: str | core.StringOut | None = None,
        workmail_action: list[WorkmailAction] | core.ArrayOut[WorkmailAction] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReceiptRule.Args(
                name=name,
                rule_set_name=rule_set_name,
                add_header_action=add_header_action,
                after=after,
                bounce_action=bounce_action,
                enabled=enabled,
                lambda_action=lambda_action,
                recipients=recipients,
                s3_action=s3_action,
                scan_enabled=scan_enabled,
                sns_action=sns_action,
                stop_action=stop_action,
                tls_policy=tls_policy,
                workmail_action=workmail_action,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        add_header_action: list[AddHeaderAction] | core.ArrayOut[AddHeaderAction] | None = core.arg(
            default=None
        )

        after: str | core.StringOut | None = core.arg(default=None)

        bounce_action: list[BounceAction] | core.ArrayOut[BounceAction] | None = core.arg(
            default=None
        )

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        lambda_action: list[LambdaAction] | core.ArrayOut[LambdaAction] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        recipients: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        rule_set_name: str | core.StringOut = core.arg()

        s3_action: list[S3Action] | core.ArrayOut[S3Action] | None = core.arg(default=None)

        scan_enabled: bool | core.BoolOut | None = core.arg(default=None)

        sns_action: list[SnsAction] | core.ArrayOut[SnsAction] | None = core.arg(default=None)

        stop_action: list[StopAction] | core.ArrayOut[StopAction] | None = core.arg(default=None)

        tls_policy: str | core.StringOut | None = core.arg(default=None)

        workmail_action: list[WorkmailAction] | core.ArrayOut[WorkmailAction] | None = core.arg(
            default=None
        )
