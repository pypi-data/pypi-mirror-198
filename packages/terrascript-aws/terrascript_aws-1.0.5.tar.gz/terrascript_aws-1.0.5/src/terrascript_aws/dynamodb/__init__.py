from .contributor_insights import ContributorInsights
from .ds_table import DsTable
from .global_table import GlobalTable
from .kinesis_streaming_destination import KinesisStreamingDestination
from .table import Table
from .table_item import TableItem
from .table_replica import TableReplica
from .tag import Tag

__all__ = [
    "TableItem",
    "Tag",
    "TableReplica",
    "KinesisStreamingDestination",
    "Table",
    "GlobalTable",
    "ContributorInsights",
    "DsTable",
]
