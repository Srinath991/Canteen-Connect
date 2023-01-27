from rest_framework import serializers
from .models import order
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        Model = order
        fields = "__all__"