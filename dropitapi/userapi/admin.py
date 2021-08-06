from django.contrib import admin

# Register your models here.
from .models import UserProfile, User, DropperProfile
admin.site.register(UserProfile)
admin.site.register(DropperProfile)
admin.site.register(User)
