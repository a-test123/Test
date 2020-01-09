from django.conf.urls import url

from move import views

urlpatterns = [
    url(r'index/',views.index),
]