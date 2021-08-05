from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank = False, unique = True,max_length = 30)
    email = models.EmailField(unique = True, blank = True)
    phone_number = models.CharField(max_length = 13, unique = True, blank = False )
    REQUIRED_FIELDS  = ['first_name', 'email', 'phone_number']

    def __str__(self):
        return '{}'.format(self.username)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'profile')
    user_age = models.IntegerField(null=False)
    user_profile_photo = models.ImageField(upload_to = 'profile_pics', blank = True)