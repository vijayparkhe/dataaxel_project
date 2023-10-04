from django.urls import path
from . import views

urlpatterns = [
    # API endpoint for sending birthday emails
    path('birthday/', views.send_birthday_emails, name='send_birthday_emails'),

]
