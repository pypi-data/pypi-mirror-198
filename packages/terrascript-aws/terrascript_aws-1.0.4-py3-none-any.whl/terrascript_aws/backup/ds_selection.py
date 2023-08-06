import terrascript.core as core


@core.data(type="aws_backup_selection", namespace="backup")
class DsSelection(core.Data):
    """
    The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the targe
    t resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devgu
    ide/access-control.html#managed-policies) for additional information about using AWS managed policie
    s or creating custom policies attached to the IAM role.
    """

    iam_role_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The display name of a resource selection document.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The backup plan ID associated with the selection of resources.
    """
    plan_id: str | core.StringOut = core.attr(str)

    """
    An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources
    to assign to a backup plan..
    """
    resources: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) The backup selection ID.
    """
    selection_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        plan_id: str | core.StringOut,
        selection_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsSelection.Args(
                plan_id=plan_id,
                selection_id=selection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        plan_id: str | core.StringOut = core.arg()

        selection_id: str | core.StringOut = core.arg()
