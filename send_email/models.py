from django.db import models

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()
    work_anniversary = models.DateField()


class EventType(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_date = models.DateField()
    is_sent = models.BooleanField(default=False)

class EmailTemplate(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
