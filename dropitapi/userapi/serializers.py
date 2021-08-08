from .models import User, UserProfile ,DropperProfile, OrdersModel
from rest_framework  import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'phone_number','profile')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"



class DropperProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropperProfile
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = "__all__"

    # def create(self,validated_data):
    #     profile_data = validated_data.pop('profile')
    #     password = validated_data.pop('password')
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     UserProfile.objects.create(user = user, **profile_data)
    #     return user



    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     profile = instance.profile

    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     profile.user_age = profile_data.get('user_age', profile.user_age)
    #     profile.user_profile_photo = profile_data.get('user_profile_photo', profile.user_profile_photo)
    #     profile.save()
    #     return instance



    