from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


#All coustoumer/dropper registraion model with fields as username, email, phone_number, first_name, last_name
class User(AbstractUser):
    username = models.CharField(blank = False, unique = True,max_length = 30)
    email = models.EmailField(unique = True, blank = True)
    phone_number = models.CharField(max_length = 10, unique = True, blank = False )
    REQUIRED_FIELDS  = ['first_name', 'email', 'phone_number']

    def __str__(self):
        return '{}'.format(self.username)


#User/coustomer profile model with fields as user_age, user_profile_photo along with user model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'profile')
    user_age = models.IntegerField(null=False)
    user_profile_photo = models.ImageField(upload_to = 'profile_pics', blank = True)
    user_gender = models.CharField(max_length=8, null=True)
    def __str__(self):
        return '{}'.format(self.user.username)

    

#dropper profile model with fields as dropper_age, droper_gender, dropper_profile_photo, dropper_authentication_number
#                                     dropper_authentication_photo, dropper_vehicle_type, dropper_rc_photo, dropper_driving_liscence_photo
class DropperProfile(models.Model):
    dropper = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'dropper')
    dropper_age = models.IntegerField(null=False)
    dropper_gender = models.CharField(max_length=8, null=True)
    dropper_profile_photo = models.ImageField(upload_to = 'profile_pics', blank = True)
    dropper_authentication_number = models.IntegerField(null=False)
    dropper_authentication_photo = models.ImageField(upload_to = 'dropper_security', blank = False) 
    dropper_vehicle_type = models.CharField(max_length = 10, blank = False )
    dropper_rc_photo = models.ImageField(upload_to = 'dropper_security', blank = False)
    dropper_driving_liscence_photo = models.ImageField(upload_to = 'dropper_security', blank = False)
    def __str__(self):
        return '{}'.format(self.dropper.username)

