from django.conf.urls import include, url
from . import views
from .models import Klient

urlpatterns = [
    url(r'^$', views.klient_list),
]
