from rest_framework import serializers
from json_store.models import WifiJson


class WifiJsonSerializer(serializers.Serializer):
    data = serializers.JSONField()
