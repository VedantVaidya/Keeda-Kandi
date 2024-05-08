from rest_framework import serializers
from json_store.models import WifiJson, WAXpathJson


class WifiJsonSerializer(serializers.Serializer):
    data = serializers.JSONField()

class WAXpathJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WAXpathJson
        fields = "__all__"


