from django.urls import path
from . import views
from .views import AppointmentTemplateView, AppointmentListView, AppointmentDetailView, AppointmentCreateView, \
    AppointmentUpdateView, AppointmentDeleteView


app_name = 'appointments'

urlpatterns = [
    path('', views.home_page_view, name='home_page'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('appointment/', AppointmentTemplateView.as_view(), name='appointment_home'),
    path('appointment_list/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointment/<int:appointment_id>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment_create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment_update/<int:appointment_id>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment_delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment_delete')
]
