#from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from . models import AlertsBody, Account, Agent, Comment, Profile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'comment', 'likes', 'dislikes')


class AlertsBodySerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = AlertsBody
        fields = ('id', 'alert_id', 'createdat', 'alerttimestamp', 'alertstate', 'external_service_id', 'rm_region', 'account', 'agent', 'comments') #reversed relationship


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'accountid', 'RemoteAccountID', 'RemoteWebServiceHost', 'remoteserviceid')


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'agentid', 'foreigndeviceguid', 'policyid', 'agentversion',  'agentstatename', 'currentdefinitionsdate', 'sdkproductversion')



class ProfileSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('phone_number', 'profession', 'user', 'photo')

