from rest_framework import serializers
from embl_interview_task_django.rest.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'age', 'favourite_colour')
