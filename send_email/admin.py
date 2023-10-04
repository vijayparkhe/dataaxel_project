from django.contrib import admin

from django.contrib import admin
from .models import Employee, EventType, Event, EmailTemplate

admin.site.register(Employee)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(EmailTemplate)
