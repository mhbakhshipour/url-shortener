from rest_framework import serializers

from url.models import Url
from client.serializers import UserSerializer


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = "__all__"
        read_only_fields = ["creator", "short_url_id"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["creator"] = UserSerializer(instance.creator, context={
                                             "request": self.context.get("request")}).data
        return response
