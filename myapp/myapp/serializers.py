# serializers.py
from rest_framework import serializers
from air.models import *

class EntityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityData
        fields = ['entity_id', 'physical_quantity', 'metric', 'value', 'ts']
