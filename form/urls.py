from django.urls import path

from form.views import Users

urlpatterns = [
    path("userdata", Users.as_view(), name='Users'),
]
