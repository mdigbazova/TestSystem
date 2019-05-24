from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from enum import Enum
from model_utils import Choices
from django.utils import timezone

from rest_framework.response import Response


# Create your models here.


#----------------------

class Profile (models.Model):
    # Now this is where the magic happens: we will now define signals so our Profile model will be
    # automatically created/updated when we create/update User instances.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField (blank=True, null=True, unique=True)
    profession = models.CharField (max_length=80, blank=True, null=True)
    photo = models.ImageField (blank=True, null=True)

    # we are hooking the create_user_profile and save_user_profile methods to the User model,
    # whenever a save event occurs. This kind of signal is called post_save
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.phone_number = request.phone_number
        user.profile.profession = request.profession
        user.profile.photo = request.photo
        user.save()

    def __str__(self):
        return f'{self.user}'

    # If you will need to access a related data, you can prefetch it in a single database query
    # users = User.objects.all().select_related('profile')


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


class AllChoices:

    def choices(em):
        return [(e.value, e.name) for e in em]


class Account (models.Model):
    accountid = models.CharField (max_length=50, verbose_name="Account ID") # "132"
    RemoteAccountID = models.CharField (max_length=50, verbose_name="Remote Account ID") # "1344"
    RemoteWebServiceHost = models.CharField (max_length=100, verbose_name="Remote WebService Host")  # "breck-alerts-api-au.system-monitor.com"
    remoteserviceid = models.CharField (max_length=50, verbose_name="Remote Service ID")
    owner = models.ForeignKey('auth.User', related_name='accounts', on_delete=models.CASCADE,
          null=True)  # related_name creates a reverse relationship

    def __str__(self):
        return f'Account ID = {self.accountid}, Remote Account ID = {self.RemoteAccountID}, Remote WebService Host = {self.RemoteWebServiceHost}'



class Agent (models.Model):
    agentid = models.CharField (max_length=10, verbose_name="Agent ID")  # "35538"
    foreigndeviceguid = models.CharField (max_length=80, verbose_name="Foreign Device GUID")  # "aa862342d9cbcfd956f74ac4c6e77ed7"
    policyid = models.CharField (max_length=10, verbose_name="Policy ID")  # "3610"
    agentversion = models.CharField (max_length=20, verbose_name="Agent Version")  # "29.0.0.1009"
    agentstatename = models.CharField (max_length=1, choices=AllChoices.choices(AgentStateType), verbose_name="Agent State Name")
    currentdefinitionsversion = models.CharField (max_length=10, null=True, blank=True, default="", verbose_name="Current Definitions Version")  # ""
    currentdefinitionsdate = models.DateTimeField(verbose_name="Current Definitions Date", default=timezone.now(), blank=True, null=True)  # "2016-08-08 11:35:52" DateField
    sdkproductversion = models.CharField(max_length=20, verbose_name="SDK Product Version")  # "5.3.28.761"
    owner = models.ForeignKey('auth.User', related_name='agents', on_delete=models.CASCADE,
            null=True)  # related_name creates a reverse relationship

    def __str__(self):
        return f'Agent ID = {self.agentid}, Agent Version = {self.agentversion}, Agent State Name = {self.get_agentstatename_display()}'



class AlertsBody (models.Model):
    class Meta:
        verbose_name = 'Alerts Body'
        verbose_name_plural = 'Alerts Bodies'

    createdat = models.DateTimeField(verbose_name="Creation Date", default=timezone.now(), blank=True)  # "2016-08-06 07:45:24" DateField, auto_now_add=True,
    alert_id = models.CharField (max_length=80, verbose_name="Alert ID")  # "e68b323d-8ef4-4f77-a7be-d23c0932b10b"
    alerttimestamp = models.DateTimeField(verbose_name="Alert Timestamp", default=timezone.now(), blank=True, null=True)  # "2016-08-06 07:45:24",DateField
    alertstate = models.CharField (max_length=1, choices=AllChoices.choices(AlertState), verbose_name="Alert State")
    external_service_id = models.CharField (max_length=1, choices=AllChoices.choices(ExternalService), verbose_name="External Service ID")
    rm_region = models.CharField(max_length=15, verbose_name="Remote Region")  # "rm_region": "hdog_aus",
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_to_alerts_body', verbose_name="Object Account")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent_to_alerts_body', verbose_name="Object Agent")
    owner = models.ForeignKey('auth.User', related_name='alerts_bodies', on_delete=models.CASCADE,
                null=True)  # related_name creates a reverse relationship

    def __str__(self):
        return f'Alert ID = {self.alert_id}; Alert State = {self.alertstate}; External Service ID = {self.external_service_id}; Region = {self.rm_region}'



class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='authors', verbose_name="Author")
    comment = models.TextField(verbose_name="Comment")
    alerts_body = models.ForeignKey(AlertsBody, on_delete=models.CASCADE, related_name='comments', verbose_name="Alerts Body")
    #likes = models.PositiveIntegerField(null=True, default=0, verbose_name="Likes")
    #dislikes = models.PositiveIntegerField(null=True, default=0, verbose_name="Dislikes")

    def __str__(self):
        return f'Author = {self.author}; Comment = {self.comment[:30]}...'

