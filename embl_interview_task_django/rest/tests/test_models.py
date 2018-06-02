from django.test import TestCase
from embl_interview_task_django.rest.models import Person


class PersonModelTests(TestCase):

    def setUp(self):
        Person.objects.create(first_name="Philip", last_name="Fry", age=25, favourite_colour="Red")

    def test_model(self):
        fry = Person.objects.get(last_name="Fry")
        self.assertEqual(fry.first_name, "Philip", "Fry is called Philip")
        self.assertEqual(fry.age, 25, "Fry is 25")
        self.assertEqual(fry.favourite_colour, "Red", "Fry's favourite colour is Red")