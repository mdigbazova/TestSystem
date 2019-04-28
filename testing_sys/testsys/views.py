from django.shortcuts import render

from rest_framework import views
from .serializers import UserCreateSerializer
from rest_framework.response import Response

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)


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

#-------------
class RegisterUser(views.APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
