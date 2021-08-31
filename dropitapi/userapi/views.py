from rest_framework import viewsets, status
from .models import User, DropperProfile, UserProfile, OrdersModel
from .serializers import UserSerializer , UserProfileSerializer , DropperProfileSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.decorators.cache import never_cache

#userlist method to view all users at once with options as get and post
@api_view(['GET'])
@never_cache
def get_user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user,many = True)
        return Response(serializer.data)

@api_view(['POST'])
@never_cache
def create_user(request):
    if request.method == 'POST':
        serializer  = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#userdetails method to view, put, delete specific users
@api_view(['GET', 'PUT', 'DELETE','POST'])
@never_cache
def get_user_details(request, pk):
    user = User.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#user_profile method to view, put, delete specific user's profile details
@api_view(['GET', 'PUT', 'DELETE','POST'])
@never_cache
def get_user_profile(request, pk):
    user_profile = UserProfile.objects.get(pk = pk)
    user = User.objects.get(pk = pk)
    if request.method == 'GET':
        UserProfile_Serializer = UserProfileSerializer(user_profile)
        User_Serializer = UserSerializer(user)
        response =dict(list((User_Serializer.data).items()) + list((UserProfile_Serializer.data).items()))
        return Response(response)

    if request.method == 'PUT':
        serializer = UserProfileSerializer(user_profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        user_profile.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


    if request.method == 'POST':
        serializer  = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#Set_user_profile function to post user profile data
@api_view(['POST'])
@never_cache
def set_user_profile(request):
        if request.method == 'POST':
            serializer  = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#_profile method to view, put, delete specific user's profile details
@api_view(['GET', 'PUT', 'DELETE','POST'])
@never_cache
def get_dropper_profile(request, pk):
    dropper_profile = DropperProfile.objects.get(pk = pk)
    user = User.objects.get(pk = pk)
    if request.method == 'GET':
        dropper_serializer = DropperProfileSerializer(dropper_profile)
        user_serializer = UserSerializer(user)
        response =dict(list((dropper_serializer.data).items())) 
        response2 =dict(list((user_serializer.data).items()))
        response.update(response2)
        return Response(response)

    if request.method == 'PUT':
        serializer = DropperProfileSerializer(dropper_profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        dropper_profile.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


    if request.method == 'POST':
        serializer  = DropperProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#Set_dropper_profile to post user profile data (posting data without primary key)
@api_view(['POST'])
@never_cache
def set_dropper_profile(request):
        if request.method == 'POST':
            serializer  = DropperProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#Order_list_view method to view all users at once with options as get and post
@api_view(['GET', 'POST'])
@never_cache
def get_order_list(request):
    if request.method == 'GET':
        orders = OrdersModel.objects.all()
        serializer = OrderSerializer(orders,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#orderdetails method to view, put, delete specific orders
@api_view(['GET', 'PUT', 'DELETE','POST'])
@never_cache
def get_order_details(request, pk):
    orders = OrdersModel.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = OrderSerializer(orders, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        orders.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def Vehicle_type(request):
    

# import pyrebase
# import os
# from django.core.files.storage import default_storage
# from django.contrib import messages
# from django.shortcuts import render, redirect



# config = {
#     "apiKey": "AIzaSyBnu-tyVi3ST-26ML0o4a6qvu4pmoQ66Kc",
#     "authDomain": "dropit-7a619.firebaseapp.com",
#     "projectId": "dropit-7a619",
#     "storageBucket": "dropit-7a619.appspot.com",
#     "messagingSenderId": "493453517133",
#     "appId": "1:493453517133:web:60bae94121607759511704",
#     "measurementId": "G-Y6X0FW2976",
#     "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()

# PATH_ON_CLOUD = "images/profile_pics"
# PATH_LOCAL = "C:/Users/jhaso/Desktop/Dropit/dropitapi/media/profile_pics/Untitled.png"

# storage.child(PATH_ON_CLOUD).put(PATH_LOCAL)


# def image_uploder(PATH_LOCAL,PATH_ON_CLOUD):
#     storage.child(PATH_ON_CLOUD).put(PATH_LOCAL)


#         # file = request.FILES['file']
#         # file_save = default_storage.save(file.name, file)
#         # storage.child("images/" + file.name).put("media/" + file.name)
#         # delete = default_storage.delete(file.name)

################################################################################################################################

