from rest_framework import serializers
from .models import AdditionalInformation


class AddInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalInformation
        fields = ['id', 'host_information', 'network', 'disk', 'memory', 'cpu', 'load_average', 'battery_charge_percentage', 'AC_power']
