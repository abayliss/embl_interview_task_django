from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from embl_interview_task_django.rest.models import Person
from embl_interview_task_django.rest.serialzers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all().order_by('last_name')
    serializer_class = PersonSerializer
