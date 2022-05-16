from django.urls import path, re_path

from accounts.api.views import TestView, UserViewSet


urlpatterns = [
    path("test/", TestView.as_view()),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='user'),
]
