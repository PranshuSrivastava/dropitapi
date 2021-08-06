from rest_framework import viewsets, status
from .models import User, DropperProfile, UserProfile
from .serializers import UserSerializer , UserProfileSerializer , DropperProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


#userlist method to view all users at once with options as get and post
@api_view(['GET', 'POST'])
def get_user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#userdetails method to view, put, delete specific users
@api_view(['GET', 'PUT', 'DELETE','POST'])
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
def get_dropper_profile(request, pk):
    dropper_profile = DropperProfile.objects.get(pk = pk)
    user = User.objects.get(pk = pk)
    if request.method == 'GET':
        dropper_serializer = DropperProfileSerializer(dropper_profile)
        user_serializer = UserSerializer(user)
        response =dict(list((dropper_serializer.data).items( + list((dropper_serializer.data).items()))) + list((user_serializer.data).items()))
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
def set_dropper_profile(request):
        if request.method == 'POST':
            serializer  = DropperProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)















###############################################################################################################################




# class UserViewS ,et(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




# @api_view(['GET'])
# def apioverview(request):
#     api_urls = {
#         'List':'/task-list/',
#         'Detail View':'/task-detail/<str:pk>/',
#         'Create':'/task-create/',
#         'Update': '/task-update/<str:pk>/',
#         'Delete': '/task-delete/<str:pk>',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all().order_by('-id')
#     serializer = TaskSerializer(tasks,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def taskDetail(request,pk):
#     tasks = Task.objects.all(id=pk)
#     serializer = TaskSerializer(tasks,many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request,pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task,data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def taskDelete(request,pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
    
#     return Response("Item successfully delete!")