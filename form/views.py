import threading
from rest_framework import generics
from form.Functions import SendEmail
from form.models import FormUser
from form.serializers import UserSerializer


class Users(generics.ListCreateAPIView):
    queryset = FormUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super(Users, self).create(request, *args, **kwargs)
        threading.Thread(target=SendEmail, args=response.data).start()
        return response
