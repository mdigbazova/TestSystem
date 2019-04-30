from django.contrib import admin
from .models import Profile, Account, Agent, AlertsBody

# Register your models here.

admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Agent)
admin.site.register(AlertsBody)


#admin.site.register(AlertState)
#admin.site.register(ExternalService)
#admin.site.register(AgentStateType)
