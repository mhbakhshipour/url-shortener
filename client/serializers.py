from rest_framework import serializers
from client.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
        read_only_fields = ["username"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["groups"] = [i.name for i in instance.groups.all()]
        return response
