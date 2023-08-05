from django.db.models import Manager

from netbox_storage.models import Partition


class PartitionManager(Manager):
    def partitions(self):
        return Partition.objects.filter(drive=self)