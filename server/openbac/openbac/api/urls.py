from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from . import views

urlpatterns = [

    url(r'cardauthrequest/$', views.Auth_request.as_view(), name='Card Auth Request from Reader to Cloud'),
    url(r'relayack/$', views.Relay_ack.as_view(), name='Relay ack for unlock request'),
    url(r'readerRegistratonRequest/$', views.ReaderBootstrap.as_view(), name='reader client bootstrap')

]
