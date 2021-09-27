from rest_framework import serializers
from form.models import FormUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormUser
        fields = '__all__'
