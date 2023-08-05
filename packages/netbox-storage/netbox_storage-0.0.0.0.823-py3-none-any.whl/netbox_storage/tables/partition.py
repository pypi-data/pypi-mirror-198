import django_tables2 as tables

from netbox.tables import (
    NetBoxTable,
    ToggleColumn,
)

from netbox_storage.models import Partition


class PartitionTable(NetBoxTable):
    """Table for displaying Partition objects."""

    pk = ToggleColumn()
    drive = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )
    size = tables.Column(
        linkify=True
    )
    type = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Partition
        fields = (
            "pk",
            "drive",
            "device",
            "size",
            "description",
        )
        default_columns = (
            "device",
            "size",
            "type",
            "description",
        )
