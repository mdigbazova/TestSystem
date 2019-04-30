from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from enum import Enum
from model_utils import Choices

from rest_framework import views
#from .serializers import UserCreateSerializer
from rest_framework.response import Response


#----------------------

#from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile (models.Model):
    # Now this is where the magic happens: we will now define signals so our Profile model will be
    # automatically created/updated when we create/update User instances.
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField (blank=True, null=True, unique=True)
    profession = models.CharField (max_length=80, blank=True, null=True)
    photo = models.ImageField (blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


#Basically we are hooking the create_user_profile and save_user_profile methods to the User model,
# whenever a save event occurs. This kind of signal is called post_save.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.location = request.location
    user.profile.birth_date = request.birth_date
    user.profile.profession = request.profession

    user.save()

#----------------------


class AlertState (Enum):
    UNDEFINED = '0'
    NEW = '1'
    RESOLVED = '2'


class ExternalService (Enum):
    # Which service is posting this event - 1 for Avery, 2 for Breck, 3 for Echo
    AVERY = '1'
    BRECK = '2'
    ECHO = '3'


class AgentStateType (Enum):
    UNKNOWN = '0'  # State has not yet been established (agent not yet installed)
    IDLE = '1'  # Agent is not running a scan and is active
    SCANNING = '2'
    SNOOZED = '3'
    DEACTIVATED = '4'
    DOWNLOADING_ENGINE = '5'
    INSTALLING_ENGINE = '6'
    ENGINE_INSTALL_FAILED = '7'
    UNINSTALLED = '8'
    INSTALLING = '9'
    INSTALL_COMPLETE = '10'
    COMPETETIVE_REMOVAL = '13'  # opswat running
    COMPETETIVE_REMOVAL_FAILED = '14'  # opswat failed
    COMPETETIVE_PRODUCT_DETECTED = '15'  # opswat identified competative product
    DOWNLOADING_COMPETETIVE_REMOVER = '16'
    INSTALLING_COMPETETIVE_REMOVER = '17'


class Account (models.Model):
    accountid = models.CharField (max_length=50)
    RemoteAccountID = models.CharField (max_length=50)
    RemoteWebServiceHost = models.CharField (max_length=100)  # "breck-alerts-api-au.system-monitor.com"
    remoteserviceid = models.CharField (max_length=50)

    def __str__(self):
        return f'Account ID = {self.accountid}, Remote WebService Host = {self.RemoteWebServiceHost}'


class Agent (models.Model):
    agentid = models.CharField (max_length=10)  # "35538"
    foreigndeviceguid = models.CharField (max_length=50)  # "aa862342d9cbcfd956f74ac4c6e77ed7"
    policyid = models.CharField (max_length=10)  # "3610"
    agentversion = models.CharField (max_length=20)  # "29.0.0.1009"
    agentstate = models.CharField (max_length=1, choices=[(tag, tag.value) for tag in AgentStateType])  # "1"
    agentstatename = models.CharField (max_length=50, choices=[(tag, tag.value) for tag in AgentStateType])  # "idle"
    currentdefinitionsversion = models.CharField (max_length=10, null=True, blank=True, default="")  # ""
    currentdefinitionsdate = models.DateField ()  # "2016-08-08 11:35:52"
    sdkproductversion = models.CharField (max_length=20)  # "5.3.28.761"

    def __str__(self):
        return f'Agent ID = {self.agentid}, Agent State Name = {self.agentstatename}'


class AlertsBody (models.Model):
    createdat = models.DateField ()  # "2016-08-06 07:45:24"
    alert_id = models.CharField (max_length=50)  # "e68b323d-8ef4-4f77-a7be-d23c0932b10b"
    alerttimestamp = models.DateField ()  # "2016-08-06 07:45:24",
    alertstate = models.CharField (max_length=1, choices=[(tag, tag.value) for tag in AlertState])
    external_service_id = models.CharField (max_length=1, choices=[(tag, tag.value) for tag in ExternalService])
    rm_region = models.CharField (max_length=15)  # "rm_region": "hdog_aus",
    account = models.ForeignKey (Account, on_delete=models.CASCADE)
    agent = models.ForeignKey (Agent, on_delete=models.CASCADE)

    # external_service_agent_id=
    # nullable integer, the agent ID this alert is associated with in the MAX DB. Will be null if alert type is not agent specific.

    def __str__(self):
        return f'Alert ID = {self.alert_id}; Alert State = {self.alertstate}; External Service ID = {self.external_service_id}; Region = {self.rm_region}'

