from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.forms import (
    CharField,
    FloatField, BooleanField
)
from django.urls import reverse_lazy

from dcim.models import Platform
from netbox.forms import (
    NetBoxModelForm,
)
from netbox_storage.models import Drive, Filesystem, Partition, PhysicalVolume, VolumeGroup, LogicalVolume, \
    MountedVolume, LinuxDevice, TemplateConfigurationDrive
from utilities.forms import (
    DynamicModelChoiceField, APISelect,
)
from virtualization.models import Cluster, ClusterType, VirtualMachine


class LVMTemplateForm(NetBoxModelForm):
    platform = DynamicModelChoiceField(
        queryset=Platform.objects.all(),
        help_text="Mapping between drive and platform  e.g. Rocky Linux 9",
    )
    drive = DynamicModelChoiceField(
        queryset=Drive.objects.all(),
        help_text="The Cluster Type of the drive",
    )
    lv_name = CharField(
        label="LV Name",
        help_text="Logical Volume Name e.g. lv_docker",
    )
    vg_name = CharField(
        label="VG Name",
        help_text="Volume Group Name e.g. vg_docker",
    )
    size = FloatField(
        label="Size (MB)",
        help_text="The size of the logical volume e.g. 25",
        validators=[MinValueValidator(0.1)],
    )
    mountpoint = CharField(
        label="Mountpoint",
        help_text="The mounted point of the volume e.g. /var/lib/docker",
    )
    fs_type = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )
    fs_options = CharField(
        required=False,
        label="Filesystem Options",
        help_text="The mounted point of the volume e.g. /var/lib/docker",
        initial='defaults',
    )
    checkbox_partition = BooleanField(
        label="Create extra partition",
        help_text="Create an extra partition e.g. /dev/sdb1",
        required=False
    )

    fieldsets = (
        (
            "Template for Platform",
            (
                "platform",
            ),
        ),
        (
            "Drive & Partition Config",
            (
                "drive",
                "checkbox_partition"
            ),
        ),
        (
            "LVM Configuration",
            (
                "lv_name",
                "vg_name",
                "size",
            ),
        ),
        (
            "Create Filesystem and mount it",
            (
                "mountpoint",
                "fs_type",
                "fs_options",
            ),
        ),
    )

    class Meta:
        model = LogicalVolume
        fields = [
            "lv_name",
            "size",
        ]

    def save(self, *args, **kwargs):
        print(f"Drive: {self.cleaned_data['drive']}")
        print(f"Platform: {self.cleaned_data['platform']}")
        print(f"LV Name: {self.cleaned_data['lv_name']}")
        print(f"VG Name: {self.cleaned_data['vg_name']}")
        print(f"Size: {self.cleaned_data['size']}")
        print(f"Mountpoint: {self.cleaned_data['mountpoint']}")
        print(f"Filesystem: {self.cleaned_data['fs_type']}")
        print(f"Filesystem Options: {self.cleaned_data['fs_options']}")
        print(f"Checkbox Partition: {self.cleaned_data['checkbox_partition']}")

        device_name_prefix = Drive.objects.get(pk=self.cleaned_data['drive'].id).device_name()
        print(f"Device Name: {device_name_prefix}")

        linux_parent_device = LinuxDevice.objects.get(device=device_name_prefix)
        if self.cleaned_data['checkbox_partition']:
            device_name = device_name_prefix + str(1)
            linuxdevice_type_pk = ContentType.objects.get(app_label='netbox_storage', model='linuxdevice').pk
            pv_linux_device = LinuxDevice.objects.create(device=device_name,
                                                         type='Partition',
                                                         size=linux_parent_device.size,
                                                         object_id=linux_parent_device.pk,
                                                         content_type_id=linuxdevice_type_pk)
        else:
            pv_linux_device = linux_parent_device

        volume_group = VolumeGroup.objects.create(vg_name=self.cleaned_data['vg_name'])

        pv = PhysicalVolume.objects.create(linux_device=pv_linux_device, vg=volume_group)

        lv_type_pk = ContentType.objects.get(app_label='netbox_storage', model='logicalvolume').pk

        self.instance.vg = volume_group
        lv = super().save(*args, **kwargs)

        linux_device_mapper = LinuxDevice.objects.create(device='/dev/mapper/vg_system-lv_home',
                                                         type='LVM',
                                                         size=pv_linux_device.size,
                                                         object_id=lv.pk,
                                                         content_type_id=lv_type_pk)

        MountedVolume.objects.create(linux_device=linux_device_mapper,
                                     mount_point=self.cleaned_data['mountpoint'],
                                     fs_type=self.cleaned_data['fs_type'],
                                     options=self.cleaned_data['fs_options'])
        return lv


#
# Add Drive template form
#
class DriveTemplateForm(NetBoxModelForm):
    size = FloatField(
        label="Size (MB)",
        help_text="The size of the logical volume e.g. 25",
        validators=[MinValueValidator(0.1)],
    )
    cluster_type = DynamicModelChoiceField(
        queryset=ClusterType.objects.all(),
        help_text="The Cluster Type of the drive",
    )
    cluster = DynamicModelChoiceField(
        queryset=Cluster.objects.all(),
        query_params={
            'type_id': '$cluster_type'  # ClusterType.objects.filter(name="Storage").values_list('id', flat=True)[0]
        },
        help_text="The Storage Cluster of the drive",
    )
    platform = DynamicModelChoiceField(
        queryset=Platform.objects.all(),
        help_text="Mapping between Volume and platform e.g. Rocky Linux 8",
    )

    fieldsets = (
        (
            "Template for Platform",
            (
                "platform",
            ),
        ),
        (
            "Drive Config",
            (
                "cluster_type",
                "cluster",
                "size",
            ),
        ),
    )

    class Meta:
        model = TemplateConfigurationDrive
        fields = [
            "platform",
        ]

    def save(self, *args, **kwargs):
        drive = Drive.objects.create(cluster=self.cleaned_data['cluster'], size=self.cleaned_data['size'])
        self.instance.drive = drive
        template_configuration = super().save(*args, **kwargs)
        drive_type_pk = ContentType.objects.get(app_label='netbox_storage', model='drive').pk
        LinuxDevice.objects.create(device=drive.device_name(),
                                   type='Disk',
                                   size=self.cleaned_data['size'],
                                   object_id=drive.pk,
                                   content_type_id=drive_type_pk)
        return template_configuration


class PartitionTemplateForm(NetBoxModelForm):
    size = FloatField(
        label="Size (MB)",
        help_text="The size of the logical volume e.g. 25",
        validators=[MinValueValidator(0.1)],
    )
    drive = DynamicModelChoiceField(
        queryset=Drive.objects.all(),
        help_text="The Cluster Type of the drive",
    )
    platform = DynamicModelChoiceField(
        queryset=Platform.objects.all(),
        help_text="Mapping between Volume and platform e.g. Rocky Linux 8",
    )
    mountpoint = CharField(
        required=False,
        label="Mountpoint",
        help_text="The mounted point of the volume e.g. /var/lib/docker",
    )
    fs_type = DynamicModelChoiceField(
        required=False,
        queryset=Filesystem.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
    )
    fs_options = CharField(
        required=False,
        label="FS Options",
        help_text="The mounted point of the volume e.g. /var/lib/docker",
    )
    label = CharField(
        required=False,
        label="Partition Label",
        help_text="The mounted point of the volume e.g. /var/lib/docker",
    )

    fieldsets = (
        (
            "Template for Platform",
            (
                "platform",
            ),
        ),
        (
            "Select drive",
            (
                "drive",
            ),
        ),
        (
            "Size of new Partition",
            (
                "size",
            ),
        ),
        (
            "Create Filesystem and mount it",
            (
                "mountpoint",
                "fs_type",
                "fs_options",
                "label",
            ),
        ),
    )

    class Meta:
        model = LinuxDevice
        fields = [
            "size"
        ]

    def save(self, *args, **kwargs):
        print(f"drive: {self.cleaned_data['drive']}")
        new_partition_count = Partition.objects.filter(drive_id=self.cleaned_data['drive'].id).count() + 1
        device_name_prefix = Drive.objects.get(pk=self.cleaned_data['drive'].id).device_name()
        print(f"Partition Count: {new_partition_count}")
        print(f"Device Name: {device_name_prefix}")
        device_name = device_name_prefix + str(new_partition_count)

        linux_device_type_pk = ContentType.objects.get(app_label='netbox_storage', model='linuxdevice').pk

        self.instance.device = device_name
        self.instance.type = 'Partition'
        self.instance.object_id = self.cleaned_data['drive'].pk
        self.instance.content_type_id = linux_device_type_pk
        linux_device_partition = super().save(*args, **kwargs)

        MountedVolume.objects.create(linux_device=linux_device_partition,
                                     mount_point=self.cleaned_data['mountpoint'],
                                     fs_type=self.cleaned_data['fs_type'],
                                     options=self.cleaned_data['fs_options'])
        return linux_device_partition


class VolumeSimpleForm(NetBoxModelForm):
    """Form for creating a new Drive object."""
    # ct = ClusterType.objects.filter(name="Storage").values_list('id', flat=True)[0]
    size = FloatField(
        label="Size (MB)",
        help_text="The size of the logical volume e.g. 25",
        validators=[MinValueValidator(0.1)],
        required=False
    )
    lv_name = CharField(
        label="LV Name",
        help_text="The logical volume name e.g. lv_data",
        required=False
    )
    vg_name = CharField(
        label="VG Name",
        help_text="The volume group name e.g. vg_data",
        required=False
    )
    mountpoint = CharField(
        label="Mountpoint",
        help_text="The mounted point of the volume e.g. /var/lib/docker",
        required=False
    )
    hard_drive_label = CharField(
        label="Hard Drive Label",
        help_text="The label of the hard drive e.g. D",
        required=False
    )
    fs = DynamicModelChoiceField(
        queryset=Filesystem.objects.all(),
        label="Filesystem Name",
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_storage-api:filesystem-list")}
        ),
        help_text="The Filesystem of the Volume e.g. ext4",
        required=False
    )
    cluster_type = DynamicModelChoiceField(
        queryset=ClusterType.objects.all(),
        help_text="The Cluster Type of the drive",
    )
    cluster = DynamicModelChoiceField(
        queryset=Cluster.objects.all(),
        query_params={
            'type_id': '$cluster_type'  # ClusterType.objects.filter(name="Storage").values_list('id', flat=True)[0]
        },
        help_text="The Storage Cluster of the drive",
    )
    description = CharField(
        required=False,
        label="Description",
        help_text="Short Description e.g. Hard Drive 1 on SSD Cluster",
    )

    class Meta:
        model = Drive

        fields = (
            "size",
            "cluster",
            "description",
        )

    def save(self, *args, **kwargs):
        drive = super().save(*args, **kwargs)
        return drive
