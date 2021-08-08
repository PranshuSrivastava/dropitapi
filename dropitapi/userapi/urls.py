from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('user-list', views.get_user_list, name="user_list"),
    path('user-details/<str:pk>/', views.get_user_details, name="user_details"),
    path('user-profile-details/<str:pk>/', views.get_user_profile, name="get_user_profile"),
    path('set-user-profile/', views.set_user_profile, name="set_user_profile"),
    path('dropper-profile/<str:pk>/', views.get_dropper_profile, name="dropper_profile"),
    path('set-dropper-profile/', views.set_dropper_profile, name="set_dropper_profile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


