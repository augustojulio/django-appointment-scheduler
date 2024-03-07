from django.db import models

class AppointmentScheduler(models.Model):
    due_date = models.DateField()
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)