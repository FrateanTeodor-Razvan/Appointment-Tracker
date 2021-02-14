from django.conf.urls import url
from . import views


app_name = 'appointments'

urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register')
]
