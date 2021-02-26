# from django.contrib.auth import views as auth_views
from django.urls import path
# from . import views
from .views import AppointmentTemplate, AppointmentList, AppointmentDetail, AppointmentCreate, \
    AppointmentUpdate, AppointmentDelete


# app_name = 'appointments'

urlpatterns = [
    # path('', views.home_page_view, name='home_page'),
    # path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('social-auth/', include('social_django.urls', namespace="social")),
    path('', AppointmentTemplate.as_view(), name='appointment_home'),
    path('list/', AppointmentList.as_view(), name='appointment_list'),
    path('detail/<int:pk>/', AppointmentDetail.as_view(), name='appointment_detail'),
    path('create/', AppointmentCreate.as_view(), name='appointment_create'),
    path('update/<int:pk>/', AppointmentUpdate.as_view(), name='appointment_update'),
    path('delete/<int:pk>/', AppointmentDelete.as_view(), name='appointment_delete')
]
