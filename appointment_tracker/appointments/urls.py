from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'appointments'

urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    path('', views.Home_PageView, name='home_page'),
    path('<int:application_id>/', views.DetailView, name='detail'),
    path('<int:application_id>/results/', views.ResultsView, name='results'),
    path('<int:application_id>/vote/', views.vote, name='vote'),
]
