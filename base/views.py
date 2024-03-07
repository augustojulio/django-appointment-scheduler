from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import AppointmentScheduler

class AppointmentList(ListView):
    model = AppointmentScheduler
    template_name = 'appointment_list.html'
    context_object_name = 'appointments'
    
class AppointmentCreate(CreateView):
    model = AppointmentScheduler
    template_name = 'appointment_form.html'
    fields = ['due_date', 'subject', 'description']
    success_url = reverse_lazy('appointment_list')
    
class AppointmentUpdate(UpdateView):
    model = AppointmentScheduler
    template_name = 'appointment_form.html'
    fields = ['due_date', 'subject', 'description']
    success_url = reverse_lazy('appointment_list')
    
class AppointmentDelete(DeleteView):
    model = AppointmentScheduler
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')