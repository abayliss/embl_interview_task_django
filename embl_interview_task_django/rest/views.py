from rest_framework import viewsets
from embl_interview_task_django.rest.models import Person
from embl_interview_task_django.rest.serialzers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('last_name')
    serializer_class = PersonSerializer
