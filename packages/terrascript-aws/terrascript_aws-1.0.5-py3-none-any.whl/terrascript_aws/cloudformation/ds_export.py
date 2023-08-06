import terrascript.core as core


@core.data(type="aws_cloudformation_export", namespace="cloudformation")
class DsExport(core.Data):
    """
    The exporting_stack_id (AWS ARNs) equivalent `ExportingStackId` from [list-exports](http://docs.aws.
    amazon.com/cli/latest/reference/cloudformation/list-exports.html)
    """

    exporting_stack_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the export as it appears in the console or from [list-exports](http://docs.aw
    s.amazon.com/cli/latest/reference/cloudformation/list-exports.html)
    """
    name: str | core.StringOut = core.attr(str)

    """
    The value from Cloudformation export identified by the export name found from [list-exports](http://
    docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)
    """
    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsExport.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
