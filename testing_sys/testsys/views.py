from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import AlertsBody
from . serializers import AlertsBodySerializer

#from rest_framework import views
#from .serializers import UserCreateSerializer


# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import Profile
#
# # Create your views here.
#
#
# #Basically we are hooking the create_user_profile and save_user_profile methods to the User model,
# # whenever a save event occurs. This kind of signal is called post_save.
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
#
# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.location = request.location
#     user.profile.birth_date = request.birth_date
#     user.profile.profession = request.profession
#
#     user.save()

#-----------------

# class RegisterUser(views.APIView):
#
#     def post(self, request):
#         serializer = UserCreateSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#-----------------

class AlertBodiesList(APIView):

    @staticmethod
    def get(self, request):
        alert_bodies = AlertsBody.objects.all()
        serializer = AlertsBodySerializer(alert_bodies, many=True)
        return Response(serializer.data)



