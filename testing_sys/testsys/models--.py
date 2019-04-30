from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from model_utils import Choices

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    profession = models.CharField (max_length=80, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


class Account(models.Model):
    accountid = models.CharField(max_length=50)
    RemoteAccountID = models.CharField(max_length=50)
    RemoteWebServiceHost = models.CharField(max_length=100) # "breck-alerts-api-au.system-monitor.com"
    remoteserviceid = models.CharField(max_length=50)

    def __str__(self):
        return f'Account ID = {self.accountid}, Remote WebService Host = {self.RemoteWebServiceHost}'


class Agent(models.Model):
    AgentStateType = (
        ('0', 'UNKNOWN'),   # State has not yet been established (agent not yet installed)
        ('1', 'IDLE'),  # Agent is not running a scan and is active
        ('2', 'SCANNING'),
        ('3', 'SNOOZED'),
        ('4', 'DEACTIVATED'),
        ('5', 'DOWNLOADING_ENGINE'),
        ('6', 'INSTALLING_ENGINE'),
        ('7', 'ENGINE_INSTALL_FAILED'),
        ('8', 'UNINSTALLED'),
        ('9', 'INSTALLING'),
        ('10', 'INSTALL_COMPLETE'),
        ('13', 'COMPETETIVE_REMOVAL'),   # opswat running
        ('14', 'COMPETETIVE_REMOVAL_FAILED'),   # opswat failed
        ('15', 'COMPETETIVE_PRODUCT_DETECTED'),   # opswat identified competative product
        ('16', 'DOWNLOADING_COMPETETIVE_REMOVER'),
        ('17', 'INSTALLING_COMPETETIVE_REMOVER')
    )

    agentid = models.CharField(max_length=10) # "35538"
    foreigndeviceguid = models.CharField(max_length=50) # "aa862342d9cbcfd956f74ac4c6e77ed7"
    policyid = models.CharField(max_length=10) #"3610"
    agentversion = models.CharField(max_length=20) # "29.0.0.1009"
    agentstate = models.CharField(max_length=1, choices=AgentStateType)
    #choices=[(tag, tag.value) for tag in AgentStateType]) #"1"
    agentstatename = models.CharField(max_length=50, choices=AgentStateType)
    #choices=[(tag, tag.value) for tag in AgentStateType]) #"idle"
    currentdefinitionsversion = models.CharField(max_length=10, null=True, blank=True) #""
    currentdefinitionsdate = models.DateField() #"2016-08-08 11:35:52"
    sdkproductversion = models.CharField(max_length=20) # "5.3.28.761"

    def __str__(self):
        return f'Agent ID = {self.agentid}, Agent State Name = {self.agentstatename}'


class AlertsBody(models.Model):
    ExternalService = (
        # Which service is posting this event - 1 for Avery, 2 for Breck, 3 for Echo
        ('1', 'AVERY'),
        ('2', 'BRECK'),
        ('3', 'ECHO')
    )

    AlertState = (
        ('0', 'UNDEFINED'),
        ('1', 'NEW'),
        ('2', 'RESOLVED')
    )

    createdat = models.DateField() # "2016-08-06 07:45:24"
    alert_id = models.CharField(max_length=50) #"e68b323d-8ef4-4f77-a7be-d23c0932b10b"
    alerttimestamp = models.DateField() #"2016-08-06 07:45:24",
    alertstate = models.CharField(max_length=1, choices=AlertState)
    #choices=[(tag, tag.value) for tag in AlertState])
    external_service_id = models.CharField(max_length=1, choices=ExternalService)
    #choices=[(tag, tag.value) for tag in ExternalService])
    rm_region = models.CharField(max_length=15) # "rm_region": "hdog_aus",
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    # external_service_agent_id=
    # nullable integer, the agent ID this alert is associated with in the MAX DB. Will be null if alert type is not agent specific.

    def __str__(self):
        return f'Alert ID = {self.alert_id}; Alert State = {self.alertstate}; External Service ID = {self.external_service_id}; Region = {self.rm_region}'



