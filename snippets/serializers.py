from rest_framework import serializers
from snippets.models import Person

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['name', 'age']
