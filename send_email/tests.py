from django.test import TestCase

# Create your tests here.
# tests.py

from django.test import TestCase
from .models import EventType, Employee, Event, EmailTemplate

class EmployeeModelTestCase(TestCase):
      def test_employee_creation(self):
            employee = Employee.objects.create(name="John",email="vijayparkhe51@gmail.com" ,birthdate="1990-01-15",work_anniversary="2020-01-01")
            self.assertEqual(employee.name, "John")
            self.assertEqual(employee.email,"vijayparkhe51@gmail.com")
            self.assertEqual(str(employee.birthdate), "1990-01-15")
            self.assertEqual(str(employee.work_anniversary),"2020-01-01")

class EventTypeModelTestCase(TestCase):
      def test_event_type_creation(self):
            event_type = EventType.objects.create(name="Birthday")
            self.assertEqual(event_type.name, "Birthday")


class EmailTemplateModelTestCase(TestCase):
    def test_email_template_creation(self):
        email_template = EmailTemplate.objects.create(subject="Happy Birthday!", message="Dear {{ employee.name }},\nHappy birthday!")
        self.assertEqual(email_template.subject, "Happy Birthday!")
        self.assertEqual(email_template.body, "Dear {{ employee.name }},\nHappy birthday!")
