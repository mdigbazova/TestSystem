#from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . models import AlertsBody


class AlertsBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertsBody
        fields = ('id', 'alerttimestamp', 'alertstate', 'external_service_id', 'rm_region')

