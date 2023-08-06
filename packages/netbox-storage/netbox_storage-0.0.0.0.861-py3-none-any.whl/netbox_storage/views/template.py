from netbox.views import generic

from netbox_storage.forms.template import LVMTemplateForm, DriveTemplateForm, \
    PartitionTemplateForm
from netbox_storage.models import TemplateConfigurationDrive, Partition, LogicalVolume, MountedVolume, LinuxDevice, \
    Drive, StorageConfigurationDrive

from django.http import HttpResponse, HttpResponseNotFound

from virtualization.models import VirtualMachine


class LVMAddTemplateView(generic.ObjectEditView):
    queryset = LogicalVolume.objects.all()
    form = LVMTemplateForm
    default_return_url = "plugins:netbox_storage:drive_list"


class AddTemplateDriveView(generic.ObjectEditView):
    queryset = TemplateConfigurationDrive.objects.all()
    form = DriveTemplateForm


class AddTemplatePartitionView(generic.ObjectEditView):
    queryset = LinuxDevice.objects.all()
    form = PartitionTemplateForm


class SyncTemplateToVMView(generic.ObjectEditView):
    queryset = StorageConfigurationDrive.objects.all()

    def get_extra_context(self, request, instance):
        print(f"Request: {request}")
        print(f"Self: {self}")
        print(f"Instance: {instance}")
        drives_id = TemplateConfigurationDrive.objects.values('drive').filter(platform=instance.platform)
        partition_dict = {}
        for drive_id in drives_id:
            drive = Drive.objects.get(pk=drive_id['drive'])

            if Partition.objects.filter(drive=drive).count() == 0:
                partition_dict[drive] = None
            else:
                partition_dict[drive] = list(Partition.objects.filter(drive=drive))

        for k, v in partition_dict.items():
            instance_drive = k
            instance_drive.pk = None
            instance_drive.save()
            StorageConfigurationDrive.objects.create(virtual_machine=instance, drive=instance_drive)

            for partition in v:
                instance_partition = partition
                instance_partition.pk = None
                instance_partition.drive = instance_drive
                instance_partition.save()
            print(k, v)
        return {}


def sys_topography_file(request):
    try:
        drives_id = TemplateConfigurationDrive.objects.values('drive').filter(platform=instance.platform)
        partition_dict = {}
        for drive_id in drives_id:
            drive = Drive.objects.get(pk=drive_id['drive'])

            if Partition.objects.filter(drive=drive).count() == 0:
                partition_dict[drive] = None
            else:
                partition_dict[drive] = list(Partition.objects.filter(drive=drive))

        for k, v in partition_dict.items():
            instance_drive = k
            instance_drive.pk = None
            instance_drive.save()
            StorageConfigurationDrive.objects.create(virtual_machine=instance, drive=instance_drive)

            for partition in v:
                instance_partition = partition
                instance_partition.pk = None
                instance_partition.drive = instance_drive
                instance_partition.save()
            print(k, v)

        print(request)
        # sending response
        response = HttpResponse('Sync finished', content_type='text/html')

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response
