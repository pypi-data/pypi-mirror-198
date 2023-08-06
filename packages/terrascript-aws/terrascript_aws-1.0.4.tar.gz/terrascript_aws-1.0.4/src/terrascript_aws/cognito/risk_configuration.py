import terrascript.core as core


@core.schema
class LowAction(core.Schema):

    event_action: str | core.StringOut = core.attr(str)

    notify: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        event_action: str | core.StringOut,
        notify: bool | core.BoolOut,
    ):
        super().__init__(
            args=LowAction.Args(
                event_action=event_action,
                notify=notify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: str | core.StringOut = core.arg()

        notify: bool | core.BoolOut = core.arg()


@core.schema
class MediumAction(core.Schema):

    event_action: str | core.StringOut = core.attr(str)

    notify: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        event_action: str | core.StringOut,
        notify: bool | core.BoolOut,
    ):
        super().__init__(
            args=MediumAction.Args(
                event_action=event_action,
                notify=notify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: str | core.StringOut = core.arg()

        notify: bool | core.BoolOut = core.arg()


@core.schema
class HighAction(core.Schema):

    event_action: str | core.StringOut = core.attr(str)

    notify: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        event_action: str | core.StringOut,
        notify: bool | core.BoolOut,
    ):
        super().__init__(
            args=HighAction.Args(
                event_action=event_action,
                notify=notify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: str | core.StringOut = core.arg()

        notify: bool | core.BoolOut = core.arg()


@core.schema
class AccountTakeoverRiskConfigurationActions(core.Schema):

    high_action: HighAction | None = core.attr(HighAction, default=None)

    low_action: LowAction | None = core.attr(LowAction, default=None)

    medium_action: MediumAction | None = core.attr(MediumAction, default=None)

    def __init__(
        self,
        *,
        high_action: HighAction | None = None,
        low_action: LowAction | None = None,
        medium_action: MediumAction | None = None,
    ):
        super().__init__(
            args=AccountTakeoverRiskConfigurationActions.Args(
                high_action=high_action,
                low_action=low_action,
                medium_action=medium_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        high_action: HighAction | None = core.arg(default=None)

        low_action: LowAction | None = core.arg(default=None)

        medium_action: MediumAction | None = core.arg(default=None)


@core.schema
class MfaEmail(core.Schema):

    html_body: str | core.StringOut = core.attr(str)

    subject: str | core.StringOut = core.attr(str)

    text_body: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        html_body: str | core.StringOut,
        subject: str | core.StringOut,
        text_body: str | core.StringOut,
    ):
        super().__init__(
            args=MfaEmail.Args(
                html_body=html_body,
                subject=subject,
                text_body=text_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        html_body: str | core.StringOut = core.arg()

        subject: str | core.StringOut = core.arg()

        text_body: str | core.StringOut = core.arg()


@core.schema
class NoActionEmail(core.Schema):

    html_body: str | core.StringOut = core.attr(str)

    subject: str | core.StringOut = core.attr(str)

    text_body: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        html_body: str | core.StringOut,
        subject: str | core.StringOut,
        text_body: str | core.StringOut,
    ):
        super().__init__(
            args=NoActionEmail.Args(
                html_body=html_body,
                subject=subject,
                text_body=text_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        html_body: str | core.StringOut = core.arg()

        subject: str | core.StringOut = core.arg()

        text_body: str | core.StringOut = core.arg()


@core.schema
class BlockEmail(core.Schema):

    html_body: str | core.StringOut = core.attr(str)

    subject: str | core.StringOut = core.attr(str)

    text_body: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        html_body: str | core.StringOut,
        subject: str | core.StringOut,
        text_body: str | core.StringOut,
    ):
        super().__init__(
            args=BlockEmail.Args(
                html_body=html_body,
                subject=subject,
                text_body=text_body,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        html_body: str | core.StringOut = core.arg()

        subject: str | core.StringOut = core.arg()

        text_body: str | core.StringOut = core.arg()


@core.schema
class NotifyConfiguration(core.Schema):

    block_email: BlockEmail | None = core.attr(BlockEmail, default=None)

    from_: str | core.StringOut | None = core.attr(str, default=None, alias="from")

    mfa_email: MfaEmail | None = core.attr(MfaEmail, default=None)

    no_action_email: NoActionEmail | None = core.attr(NoActionEmail, default=None)

    reply_to: str | core.StringOut | None = core.attr(str, default=None)

    source_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source_arn: str | core.StringOut,
        block_email: BlockEmail | None = None,
        from_: str | core.StringOut | None = None,
        mfa_email: MfaEmail | None = None,
        no_action_email: NoActionEmail | None = None,
        reply_to: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NotifyConfiguration.Args(
                source_arn=source_arn,
                block_email=block_email,
                from_=from_,
                mfa_email=mfa_email,
                no_action_email=no_action_email,
                reply_to=reply_to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_email: BlockEmail | None = core.arg(default=None)

        from_: str | core.StringOut | None = core.arg(default=None)

        mfa_email: MfaEmail | None = core.arg(default=None)

        no_action_email: NoActionEmail | None = core.arg(default=None)

        reply_to: str | core.StringOut | None = core.arg(default=None)

        source_arn: str | core.StringOut = core.arg()


@core.schema
class AccountTakeoverRiskConfiguration(core.Schema):

    actions: AccountTakeoverRiskConfigurationActions = core.attr(
        AccountTakeoverRiskConfigurationActions
    )

    notify_configuration: NotifyConfiguration = core.attr(NotifyConfiguration)

    def __init__(
        self,
        *,
        actions: AccountTakeoverRiskConfigurationActions,
        notify_configuration: NotifyConfiguration,
    ):
        super().__init__(
            args=AccountTakeoverRiskConfiguration.Args(
                actions=actions,
                notify_configuration=notify_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: AccountTakeoverRiskConfigurationActions = core.arg()

        notify_configuration: NotifyConfiguration = core.arg()


@core.schema
class CompromisedCredentialsRiskConfigurationActions(core.Schema):

    event_action: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        event_action: str | core.StringOut,
    ):
        super().__init__(
            args=CompromisedCredentialsRiskConfigurationActions.Args(
                event_action=event_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_action: str | core.StringOut = core.arg()


@core.schema
class CompromisedCredentialsRiskConfiguration(core.Schema):

    actions: CompromisedCredentialsRiskConfigurationActions = core.attr(
        CompromisedCredentialsRiskConfigurationActions
    )

    event_filter: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        actions: CompromisedCredentialsRiskConfigurationActions,
        event_filter: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=CompromisedCredentialsRiskConfiguration.Args(
                actions=actions,
                event_filter=event_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: CompromisedCredentialsRiskConfigurationActions = core.arg()

        event_filter: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class RiskExceptionConfiguration(core.Schema):

    blocked_ip_range_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skipped_ip_range_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        blocked_ip_range_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        skipped_ip_range_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=RiskExceptionConfiguration.Args(
                blocked_ip_range_list=blocked_ip_range_list,
                skipped_ip_range_list=skipped_ip_range_list,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        blocked_ip_range_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        skipped_ip_range_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_cognito_risk_configuration", namespace="cognito")
class RiskConfiguration(core.Resource):
    """
    (Optional) The account takeover risk configuration. See details below.
    """

    account_takeover_risk_configuration: AccountTakeoverRiskConfiguration | None = core.attr(
        AccountTakeoverRiskConfiguration, default=None
    )

    """
    (Optional) The app client ID. When the client ID is not provided, the same risk configuration is app
    lied to all the clients in the User Pool.
    """
    client_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The compromised credentials risk configuration. See details below.
    """
    compromised_credentials_risk_configuration: CompromisedCredentialsRiskConfiguration | None = (
        core.attr(CompromisedCredentialsRiskConfiguration, default=None)
    )

    """
    The user pool ID. or The user pool ID and Client Id separated by a `:` if the configuration is clien
    t specific.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The configuration to override the risk decision. See details below.
    """
    risk_exception_configuration: RiskExceptionConfiguration | None = core.attr(
        RiskExceptionConfiguration, default=None
    )

    """
    (Required) The user pool ID.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_pool_id: str | core.StringOut,
        account_takeover_risk_configuration: AccountTakeoverRiskConfiguration | None = None,
        client_id: str | core.StringOut | None = None,
        compromised_credentials_risk_configuration: CompromisedCredentialsRiskConfiguration
        | None = None,
        risk_exception_configuration: RiskExceptionConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RiskConfiguration.Args(
                user_pool_id=user_pool_id,
                account_takeover_risk_configuration=account_takeover_risk_configuration,
                client_id=client_id,
                compromised_credentials_risk_configuration=compromised_credentials_risk_configuration,
                risk_exception_configuration=risk_exception_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_takeover_risk_configuration: AccountTakeoverRiskConfiguration | None = core.arg(
            default=None
        )

        client_id: str | core.StringOut | None = core.arg(default=None)

        compromised_credentials_risk_configuration: CompromisedCredentialsRiskConfiguration | None = core.arg(
            default=None
        )

        risk_exception_configuration: RiskExceptionConfiguration | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()
