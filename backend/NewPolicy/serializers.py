from rest_framework import serializers
from .models import NewPolicy
class NewPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model= NewPolicy
        fields=("__all__")