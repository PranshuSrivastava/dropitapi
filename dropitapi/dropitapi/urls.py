# from django.conf.urls import include, url
# from django.contrib import admin
# urlpatterns = [
#     url('admin/', admin.site.urls),
#     url('user/', include('dropitapi.urls')),
# ]

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('userapi.urls')),
]