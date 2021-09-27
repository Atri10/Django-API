from django.urls import path
from form.views import Users

urlpatterns = [
    path("viewall", Users.as_view(), name='Users'),
]
