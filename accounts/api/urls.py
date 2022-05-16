from django.urls import path

from accounts.api.views import (
    TestView, 
    UserViewSet, 
    LoginAuthToken
)


urlpatterns = [
    path("test/", TestView.as_view()),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='user'),
    path('login/', LoginAuthToken.as_view(), name='login'),
]
