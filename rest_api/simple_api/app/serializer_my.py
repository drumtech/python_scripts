from rest_framework import serializers
from .models import Server


class ServerSerializer_my(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['ip_address', 'server_is_active']

