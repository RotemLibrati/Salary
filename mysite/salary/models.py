from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user_id = models.CharField(max_length=50)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100, default="")
    is_admin = models.BooleanField(default=False)
    payment = models.IntegerField(default=29)


    def __str__(self):
        return str(self.user)