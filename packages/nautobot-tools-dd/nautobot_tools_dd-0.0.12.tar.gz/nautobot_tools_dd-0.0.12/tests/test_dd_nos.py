import os
import pdb

from django.test import TestCase
from nautobot.dcim.models import Device, Site, DeviceRole, DeviceType, Manufacturer
from nautobot.extras.models import StatusModel, Status
from rest_framework import serializers
from yangson import DataModel
from yangson.datatype import Decimal64Type

from nautobot_tools.serializers import YANGModelSerializer
from nautobot_tools.utils import get_model


class NOSTestCase(TestCase):
    def test_yangson_debug(self):
        model = get_model(
            'tests/example_files/ex2', 'yang-library-ex2.json',
            (".", "../yang-modules/ietf")
        )
        # temporary playground here
        t = model.children[0].children[2].type
        self.assertTrue(isinstance(t, Decimal64Type))

    def test_nautobot_object_scanner_yang_ref(self):
        # ===== initial data =====
        # manufacturer
        manufacturer_data = {
            "name": "Cisco",
            "slug": "cisco"
        }
        manufacturer_object = Manufacturer.objects.create(**manufacturer_data)

        # device type
        device_type_data = {
            "manufacturer": manufacturer_object,
            "model": "Catalyst 4500",
            "slug": "catalyst-4500",
            "u_height": 10,
            "is_full_depth": True
        }
        device_type_object = DeviceType.objects.create(**device_type_data)

        # device role
        device_role_data = {
            "name": "Access",
            "slug": "access",
            "color": "c0c0c0",
            "vm_role": False
        }
        device_role_object = DeviceRole.objects.create(**device_role_data)

        # status
        status_object = Status.objects.first()

        # site
        site_data = {
            "status": status_object,
            "name": "Cisco DK Lab",
            "slug": "cisco-dk-lab",
        }
        site_object = Site.objects.create(**site_data)

        # device
        device_data = {
            "name": "c4500",
            "device_role": device_role_object,
            "device_type": device_type_object,
            "site": site_object,
            "status": status_object,
        }
        device = Device.objects.create(**device_data)
        self.assertTrue(
            Device.objects.filter(**device_data).exists()
        )

        class ExampleSerializer(YANGModelSerializer):
            class Meta:
                model = get_model('tests/example_files/nautobot_ref', 'yang-library.json')
                fields = '__all__'

            def run(self, validated_data):
                device_obj: Device = validated_data['nautobot-ref:device-name-update']['device']
                device_obj.name = validated_data['nautobot-ref:device-name-update']['name']
                device_obj.save()
                return True

        # ===== test =====
        data = {
            'nautobot-ref:device-name-update': {
                'device': device.id,
                'name': device_data['name'] + "_Updated",
            }
        }
        example_serializer = ExampleSerializer(data=data)
        example_serializer.is_valid(raise_exception=True)
        self.assertEqual(example_serializer.validated_data['nautobot-ref:device-name-update']['device'].name,
                         device_data['name'])

        example_serializer.save()
        self.assertEqual(
            example_serializer.validated_data['nautobot-ref:device-name-update']['device'].name,
            data['nautobot-ref:device-name-update']['name']
        )
