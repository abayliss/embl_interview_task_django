from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from embl_interview_task_django.rest.models import Person


class PersonApiTest(APITestCase):

    fixtures = ['admin_user', 'people']

    def test_auth_fail(self):
        data = {
            'first_name': 'Bender',
            'last_name': 'Rodriguez',
            'age': 4,
            'favourite_colour': "Grey"
        }

        # ensure we aren't sending an auth header
        self.client.logout()
        response = self.client.post("/person/", data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        data = {
            'first_name': 'Bender',
            'last_name': 'Rodriguez',
            'age': 4,
            'favourite_colour': "Grey"
        }

        self.client.force_authenticate(user=User.objects.get(username='admin'))
        response = self.client.post('/person/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.get(first_name='Bender').last_name, 'Rodriguez')

    def test_get(self):
        self.client.force_authenticate(user=User.objects.get(username='admin'))
        response = self.client.get('/person/1/')

        self.assertEqual(response.data['first_name'], 'Turanga')
        self.assertEqual(response.data['last_name'], 'Leela')

    def test_list(self):
        self.client.force_authenticate(user=User.objects.get(username='admin'))
        response = self.client.get('/person/')

        self.assertEqual(len(response.data), 2)

    def test_delete(self):
        self.client.force_authenticate(user=User.objects.get(username='admin'))
        response = self.client.delete('/person/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Person.DoesNotExist, Person.objects.get, first_name='Turanga')