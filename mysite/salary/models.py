from datetime import datetime

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

class Shifts(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, default=1)
    date = models.DateField()
    start = models.TimeField()
    over = models.TimeField()
    percent100 = models.IntegerField(default=0)
    percent125 = models.IntegerField(default=0)
    percent150 = models.IntegerField(default=0)
    percent175 = models.IntegerField(default=0)
    percent200 = models.IntegerField(default=0)
    total_time = models.FloatField(default=0)
    total_money = models.FloatField(default=0)
    bonus = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000, blank=True)
#    rest = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)