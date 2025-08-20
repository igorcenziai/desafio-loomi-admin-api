from rest_framework import serializers
from .models import Tinta

class TintaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tinta
        fields = '__all__'
        read_only_fields = ['id']