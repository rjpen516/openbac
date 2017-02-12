from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from . import views

urlpatterns = [

    url(r'deviceAuth/$', views.Auth_request.as_view(), name='Device Auth')

]