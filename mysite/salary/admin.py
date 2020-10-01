from django.contrib import admin

# Register your models here.
from .models import Users, UserProfile
admin.site.register(Users)
admin.site.register(UserProfile)