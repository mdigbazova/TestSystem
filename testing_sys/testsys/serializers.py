from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from . models import AlertsBody, Account, Agent, Comment, Profile


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

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

#----------------------


class OwnerSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
            default=serializers.CurrentUserDefault(),
            required=False,
            allow_null=True
        )

    def validate_owner(self, value):
        return self.context['request'].user

#----------------------



class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        #fields = ('__all__')
        fields = ('id', 'accountid', 'RemoteAccountID', 'RemoteWebServiceHost', 'remoteserviceid', 'owner')


class AccountCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        #import pdb; pdb.set_trace()
        model = Account
        fields = ('accountid', 'RemoteAccountID', 'RemoteWebServiceHost', 'remoteserviceid', 'owner')

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        validated_data['owner'] = self.context['request'].user
        return super(AccountCreateSerializer, self).create(validated_data)

#---------------------


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        #fields = ('__all__')
        fields = ('id', 'agentid', 'foreigndeviceguid', 'policyid', 'agentversion',  'agentstatename', 'currentdefinitionsdate', 'sdkproductversion', 'owner')


class AgentCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Agent
        fields = ('agentid', 'foreigndeviceguid', 'policyid', 'agentversion',  'agentstatename', 'currentdefinitionsdate', 'sdkproductversion', 'owner')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        validated_data['owner'] = self.context['request'].user
        return super (AgentCreateSerializer, self).create(validated_data)


#---------------------


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'comment') #, 'likes', 'dislikes'

#---------------------


class AlertsBodySerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = AlertsBody
        fields = ('__all__')


class AlertsBodyCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = AlertsBody
        fields = ('alert_id', 'createdat', 'alerttimestamp', 'alertstate', 'external_service_id', 'rm_region', 'account', 'agent', 'owner', 'comments') #reversed relationship

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        validated_data['owner'] = self.context['request'].user
        return super(AlertsBodyCreateSerializer, self).create(validated_data)


#---------------------


class ProfileSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('phone_number', 'profession', 'user', 'photo')

