from django.urls import path, re_path

from accounts.api.views import TestView


urlpatterns = [
    path("test/", TestView.as_view()),
]
