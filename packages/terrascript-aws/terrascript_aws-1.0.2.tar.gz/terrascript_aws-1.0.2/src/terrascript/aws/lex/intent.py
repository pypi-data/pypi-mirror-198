import terrascript.core as core


@core.schema
class Message(core.Schema):

    content: str | core.StringOut = core.attr(str)

    content_type: str | core.StringOut = core.attr(str)

    group_number: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        content: str | core.StringOut,
        content_type: str | core.StringOut,
        group_number: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Message.Args(
                content=content,
                content_type=content_type,
                group_number=group_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: str | core.StringOut = core.arg()

        content_type: str | core.StringOut = core.arg()

        group_number: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ValueElicitationPrompt(core.Schema):

    max_attempts: int | core.IntOut = core.attr(int)

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: int | core.IntOut,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ValueElicitationPrompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: int | core.IntOut = core.arg()

        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Slot(core.Schema):

    description: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    priority: int | core.IntOut | None = core.attr(int, default=None)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    sample_utterances: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    slot_constraint: str | core.StringOut = core.attr(str)

    slot_type: str | core.StringOut = core.attr(str)

    slot_type_version: str | core.StringOut | None = core.attr(str, default=None)

    value_elicitation_prompt: ValueElicitationPrompt | None = core.attr(
        ValueElicitationPrompt, default=None
    )

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        slot_constraint: str | core.StringOut,
        slot_type: str | core.StringOut,
        description: str | core.StringOut | None = None,
        priority: int | core.IntOut | None = None,
        response_card: str | core.StringOut | None = None,
        sample_utterances: list[str] | core.ArrayOut[core.StringOut] | None = None,
        slot_type_version: str | core.StringOut | None = None,
        value_elicitation_prompt: ValueElicitationPrompt | None = None,
    ):
        super().__init__(
            args=Slot.Args(
                name=name,
                slot_constraint=slot_constraint,
                slot_type=slot_type,
                description=description,
                priority=priority,
                response_card=response_card,
                sample_utterances=sample_utterances,
                slot_type_version=slot_type_version,
                value_elicitation_prompt=value_elicitation_prompt,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        priority: int | core.IntOut | None = core.arg(default=None)

        response_card: str | core.StringOut | None = core.arg(default=None)

        sample_utterances: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        slot_constraint: str | core.StringOut = core.arg()

        slot_type: str | core.StringOut = core.arg()

        slot_type_version: str | core.StringOut | None = core.arg(default=None)

        value_elicitation_prompt: ValueElicitationPrompt | None = core.arg(default=None)


@core.schema
class ConclusionStatement(core.Schema):

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConclusionStatement.Args(
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CodeHook(core.Schema):

    message_version: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        message_version: str | core.StringOut,
        uri: str | core.StringOut,
    ):
        super().__init__(
            args=CodeHook.Args(
                message_version=message_version,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_version: str | core.StringOut = core.arg()

        uri: str | core.StringOut = core.arg()


@core.schema
class FulfillmentActivity(core.Schema):

    code_hook: CodeHook | None = core.attr(CodeHook, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        code_hook: CodeHook | None = None,
    ):
        super().__init__(
            args=FulfillmentActivity.Args(
                type=type,
                code_hook=code_hook,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_hook: CodeHook | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class Prompt(core.Schema):

    max_attempts: int | core.IntOut = core.attr(int)

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: int | core.IntOut,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Prompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: int | core.IntOut = core.arg()

        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RejectionStatement(core.Schema):

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RejectionStatement.Args(
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.schema
class FollowUpPrompt(core.Schema):

    prompt: Prompt = core.attr(Prompt)

    rejection_statement: RejectionStatement = core.attr(RejectionStatement)

    def __init__(
        self,
        *,
        prompt: Prompt,
        rejection_statement: RejectionStatement,
    ):
        super().__init__(
            args=FollowUpPrompt.Args(
                prompt=prompt,
                rejection_statement=rejection_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prompt: Prompt = core.arg()

        rejection_statement: RejectionStatement = core.arg()


@core.schema
class DialogCodeHook(core.Schema):

    message_version: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        message_version: str | core.StringOut,
        uri: str | core.StringOut,
    ):
        super().__init__(
            args=DialogCodeHook.Args(
                message_version=message_version,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_version: str | core.StringOut = core.arg()

        uri: str | core.StringOut = core.arg()


@core.schema
class ConfirmationPrompt(core.Schema):

    max_attempts: int | core.IntOut = core.attr(int)

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: int | core.IntOut,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConfirmationPrompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: int | core.IntOut = core.arg()

        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_lex_intent", namespace="aws_lex")
class Intent(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    checksum: str | core.StringOut = core.attr(str, computed=True)

    conclusion_statement: ConclusionStatement | None = core.attr(ConclusionStatement, default=None)

    confirmation_prompt: ConfirmationPrompt | None = core.attr(ConfirmationPrompt, default=None)

    create_version: bool | core.BoolOut | None = core.attr(bool, default=None)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    dialog_code_hook: DialogCodeHook | None = core.attr(DialogCodeHook, default=None)

    follow_up_prompt: FollowUpPrompt | None = core.attr(FollowUpPrompt, default=None)

    fulfillment_activity: FulfillmentActivity = core.attr(FulfillmentActivity)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    parent_intent_signature: str | core.StringOut | None = core.attr(str, default=None)

    rejection_statement: RejectionStatement | None = core.attr(RejectionStatement, default=None)

    sample_utterances: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    slot: list[Slot] | core.ArrayOut[Slot] | None = core.attr(
        Slot, default=None, kind=core.Kind.array
    )

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        fulfillment_activity: FulfillmentActivity,
        name: str | core.StringOut,
        conclusion_statement: ConclusionStatement | None = None,
        confirmation_prompt: ConfirmationPrompt | None = None,
        create_version: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        dialog_code_hook: DialogCodeHook | None = None,
        follow_up_prompt: FollowUpPrompt | None = None,
        parent_intent_signature: str | core.StringOut | None = None,
        rejection_statement: RejectionStatement | None = None,
        sample_utterances: list[str] | core.ArrayOut[core.StringOut] | None = None,
        slot: list[Slot] | core.ArrayOut[Slot] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Intent.Args(
                fulfillment_activity=fulfillment_activity,
                name=name,
                conclusion_statement=conclusion_statement,
                confirmation_prompt=confirmation_prompt,
                create_version=create_version,
                description=description,
                dialog_code_hook=dialog_code_hook,
                follow_up_prompt=follow_up_prompt,
                parent_intent_signature=parent_intent_signature,
                rejection_statement=rejection_statement,
                sample_utterances=sample_utterances,
                slot=slot,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        conclusion_statement: ConclusionStatement | None = core.arg(default=None)

        confirmation_prompt: ConfirmationPrompt | None = core.arg(default=None)

        create_version: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        dialog_code_hook: DialogCodeHook | None = core.arg(default=None)

        follow_up_prompt: FollowUpPrompt | None = core.arg(default=None)

        fulfillment_activity: FulfillmentActivity = core.arg()

        name: str | core.StringOut = core.arg()

        parent_intent_signature: str | core.StringOut | None = core.arg(default=None)

        rejection_statement: RejectionStatement | None = core.arg(default=None)

        sample_utterances: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        slot: list[Slot] | core.ArrayOut[Slot] | None = core.arg(default=None)
