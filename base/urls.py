from django.urls import path
from .views import AppointmentList, AppointmentCreate, AppointmentUpdate, AppointmentDelete

urlpatterns = [
    path('', AppointmentList.as_view(), name='appointment_list'),
    path('new/', AppointmentCreate.as_view(), name='appointment_new'),
    path('edit/<int:pk>/', AppointmentUpdate.as_view(), name='appointment_edit'),
    path('delete/<int:pk>/', AppointmentDelete.as_view(), name='appointment_delete'),
]
