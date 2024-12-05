from rest_framework import serializers
from.models import programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields= ('fullname','nickname','ege')
        fields= '__all__'