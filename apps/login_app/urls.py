from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate$', views.validate),
    url(r'^register$', views.register),
    url(r'^verify$', views.verify),
    url(r'^login$', views.login),
]
