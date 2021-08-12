from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_active_bidding_orders/', views.update_active_bidding_orders, name="update_time"),
    # path('update1/', views.update_active1, name="update_time"),
  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


