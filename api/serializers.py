from rest_framework import serializers
from core.models import KhojTheSearch


class KhojSerializers(serializers.ModelSerializer):
    class Meta:
        model = KhojTheSearch
        fields = '__all__'