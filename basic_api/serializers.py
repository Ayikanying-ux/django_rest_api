from rest_framework import serializers
from basic_api.models import DRFPost

class DRFPostSerializer(serializers.Serializer):
    class Meta:
        model = DRFPost
        fields = '__all__'