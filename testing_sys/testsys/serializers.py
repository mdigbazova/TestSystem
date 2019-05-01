#from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . models import AlertsBody, Account, Agent


class AlertsBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertsBody
        fields = ('id', 'alert_id', 'createdat', 'alerttimestamp', 'alertstate', 'external_service_id', 'rm_region', 'account', 'agent')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'accountid', 'RemoteAccountID', 'RemoteWebServiceHost', 'remoteserviceid')


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'agentid', 'foreigndeviceguid', 'policyid', 'agentversion',  'agentstatename', 'currentdefinitionsdate', 'sdkproductversion')

