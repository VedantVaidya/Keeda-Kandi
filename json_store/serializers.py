from rest_framework import serializers
from json_store.models import WifiJson, WAXpathJson, WAScriptJson


class WifiJsonSerializer(serializers.Serializer):
    data = serializers.JSONField()

class WAXpathJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WAXpathJson
        fields = "__all__"


class WAScriptJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WAScriptJson
        fields = "__all__"


