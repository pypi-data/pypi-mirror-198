import terrascript.core as core


@core.schema
class DagEdge(core.Schema):

    source: str | core.StringOut = core.attr(str)

    target: str | core.StringOut = core.attr(str)

    target_parameter: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        source: str | core.StringOut,
        target: str | core.StringOut,
        target_parameter: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DagEdge.Args(
                source=source,
                target=target,
                target_parameter=target_parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source: str | core.StringOut = core.arg()

        target: str | core.StringOut = core.arg()

        target_parameter: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Args(core.Schema):

    name: str | core.StringOut = core.attr(str)

    param: bool | core.BoolOut | None = core.attr(bool, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
        param: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Args.Args(
                name=name,
                value=value,
                param=param,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        param: bool | core.BoolOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.schema
class DagNode(core.Schema):

    args: list[Args] | core.ArrayOut[Args] = core.attr(Args, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str)

    line_number: int | core.IntOut | None = core.attr(int, default=None)

    node_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        args: list[Args] | core.ArrayOut[Args],
        id: str | core.StringOut,
        node_type: str | core.StringOut,
        line_number: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DagNode.Args(
                args=args,
                id=id,
                node_type=node_type,
                line_number=line_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        args: list[Args] | core.ArrayOut[Args] = core.arg()

        id: str | core.StringOut = core.arg()

        line_number: int | core.IntOut | None = core.arg(default=None)

        node_type: str | core.StringOut = core.arg()


@core.data(type="aws_glue_script", namespace="glue")
class DsScript(core.Data):
    """
    (Required) A list of the edges in the DAG. Defined below.
    """

    dag_edge: list[DagEdge] | core.ArrayOut[DagEdge] = core.attr(DagEdge, kind=core.Kind.array)

    """
    (Required) A list of the nodes in the DAG. Defined below.
    """
    dag_node: list[DagNode] | core.ArrayOut[DagNode] = core.attr(DagNode, kind=core.Kind.array)

    """
    (Required) A node identifier that is unique within the node's graph.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid
    values are `PYTHON` and `SCALA`.
    """
    language: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
    """
    python_script: str | core.StringOut = core.attr(str, computed=True)

    """
    The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
    """
    scala_code: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        dag_edge: list[DagEdge] | core.ArrayOut[DagEdge],
        dag_node: list[DagNode] | core.ArrayOut[DagNode],
        language: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsScript.Args(
                dag_edge=dag_edge,
                dag_node=dag_node,
                language=language,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dag_edge: list[DagEdge] | core.ArrayOut[DagEdge] = core.arg()

        dag_node: list[DagNode] | core.ArrayOut[DagNode] = core.arg()

        language: str | core.StringOut | None = core.arg(default=None)
