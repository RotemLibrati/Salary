from django.contrib import admin

# Register your models here.
from .models import Users, UserProfile, Shifts
admin.site.register(Users)
admin.site.register(UserProfile)
admin.site.register(Shifts)