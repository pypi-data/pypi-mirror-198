from netbox.views import generic

from netbox_storage.forms.template import LVMTemplateForm, DriveTemplateForm, \
    PartitionTemplateForm
from netbox_storage.models import TemplateConfigurationDrive, Partition, LogicalVolume, MountedVolume, LinuxDevice


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


class SyncTemplateToVMView(generic.ObjectView):
    print("Hello")
