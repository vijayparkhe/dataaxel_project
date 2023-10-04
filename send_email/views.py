
from django.shortcuts import HttpResponse

from send_email.tasks import send_birthday_greetings
def send_birthday_emails(request):
    send_birthday_greetings.delay()
    return HttpResponse("Birthday emails sent successfully.")
