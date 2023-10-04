# yourapp/tasks.py
from send_email.models import *
from celery import shared_task
from celery_project import settings
from datetime import datetime
from django.core.mail import send_mail
from django.db.models import Q
@shared_task(bind=True)
def send_birthday_greetings(self):
    today = datetime.today()
    birthday_employees = Employee.objects.filter(birthdate__month=today.month, birthdate__day=today.day)
        
    # Iterate through birthday employees and send emails
    for employee in birthday_employees:
        # Get the birthday email template (assuming you have an email template for birthdays)
        template = EmailTemplate.objects.get(event_type__name="Birthday")

        # Compose the email subject and message
        subject = template.subject
        message = template.message.format(employee_name=employee.name)


        # Send the email
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[employee.email],fail_silently=True)
    return'Done-send_birthday_greetngs_tasks'
