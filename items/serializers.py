from .models import item
from rest_framework.serializers import ModelSerializer
class itemsserializer(ModelSerializer):
    class Meta:
        model=item
        fields='__all__'