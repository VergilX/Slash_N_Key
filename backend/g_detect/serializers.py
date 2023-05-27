from rest_framework import serializers
from .models import Garbage

class GarbageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garbage
        fields = ['id', 'location']

    def create(self, validated_data):
        return Garbage.objects.create(**validated_data)

