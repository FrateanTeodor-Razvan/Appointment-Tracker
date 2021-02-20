from django.urls import path
from . import views
from .views import AppointmentTemplate, AppointmentList, AppointmentDetail, AppointmentCreate, \
    AppointmentUpdate, AppointmentDelete


# app_name = 'appointments'

urlpatterns = [
    path('', views.home_page_view, name='home_page'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('appointment/', AppointmentTemplate.as_view(), name='appointment_home'),
    path('appointment_list/', AppointmentList.as_view(), name='appointment_list'),
    path('appointment/<int:appointment_id>/', AppointmentDetail.as_view(), name='appointment_detail'),
    path('appointment_create/', AppointmentCreate.as_view(), name='appointment_create'),
    path('appointment_update/<int:appointment_id>/', AppointmentUpdate.as_view(), name='appointment_update'),
    path('appointment_delete/<int:appointment_id>/', AppointmentDelete.as_view(), name='appointment_delete')
]
