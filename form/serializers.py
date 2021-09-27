from rest_framework import serializers
from form.models import FormUser


def validate(phone):
    if len(phone) > 12:
        raise serializers.ValidationError("Incorrect Phone Number")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormUser
        fields = '__all__'
