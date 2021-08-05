# from django.conf.urls import url, include
# from rest_framework import routers
# from api.views import UserViewSet

# # router = routers.DefaultRouter()
# # router.register('users', UserViewSet)

# urlpatterns = [
#     url('register/', include(router.urls)),
# ]


from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]