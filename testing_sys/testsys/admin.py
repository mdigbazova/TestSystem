from django.contrib import admin
from .models import Profile, Account, Agent, AlertsBody, Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Agent)
admin.site.register(AlertsBody)
admin.site.register(Comment)

