from rest_framework import serializers
from CBVAPI.models import Studentdbs

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Studentdbs
        fields = ['id','name','score','age']
