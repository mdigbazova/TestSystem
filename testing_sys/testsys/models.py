from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #phone = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    profession = models.CharField (max_length=80, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

