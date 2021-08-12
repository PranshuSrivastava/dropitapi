from rest_framework import viewsets, status
from .models import Bid, BidManager, Auction, AuctionManager,IsActiveManager
# from .serializers import UserSerializer , UserProfileSerializer , DropperProfileSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from datetime import datetime, timedelta

# # Create your views here.
def update_active(request):
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    expired_bid_ids = Auction.objects.values_list('expiry_date', flat=True)
    print("############################################################################################################################")
    for val in expired_bid_ids:
        if (val.time() < current_time) ==True:
            print(current_time  ,val.time())
    print("###########################################################################################################################")
















# # Create your views here.
def update_active(request):
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    expired_bid_ids = Auction.objects.values_list('expiry_date', flat=True)
    print("############################################################################################################################")
    for val in expired_bid_ids:
        if (val.time() < current_time) ==True:
            print(current_time  ,val.time())
    print("###########################################################################################################################")
















# # # # # Create your views here.
# def update_active(request):
#     current_time = datetime.now().time()
#     expired_bid_ids = Auction.objects.all().get(user=Auction.expiry_date)
#     print("#######################################################################################################################3#")
#     print(expired_bid_ids[0].time() > current_time)
#     print(current_time  ,expired_bid_ids[0].time())
#     # expired_abc = Auction.objects.all()
#     print("###########################################################################################################################")

    

#filter(Auction.expiry_date>current_time).values_list('id', flat=True)

# @api_view(['GET', 'PUT', 'DELETE','POST'])
# @never_cache
# def get_dropper_profile(request, pk):
#     dropper_profile = DropperProfile.objects.get(pk = pk)
#     user = User.objects.get(pk = pk)
#     if request.method == 'GET':
#         dropper_serializer = DropperProfileSerializer(dropper_profile)
#         user_serializer = UserSerializer(user)
#         response =dict(list((dropper_serializer.data).items( + list((dropper_serializer.data).items()))) + list((user_serializer.data).items()))
#         return Response(response)

#     if request.method == 'PUT':
#         serializer = DropperProfileSerializer(dropper_profile, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         dropper_profile.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


#     if request.method == 'POST':
#         serializer  = DropperProfileSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# #orderdetails method to view, put, delete specific orders
# @api_view(['GET', 'PUT', 'DELETE','POST'])
# @never_cache
# def get_order_details(request, pk):
#     orders = OrdersModel.objects.get(pk = pk)
#     if request.method == 'GET':
#         serializer = OrderSerializer(orders)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = OrderSerializer(orders, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         orders.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
