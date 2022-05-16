
from urllib import response
from django.db.models.query import EmptyQuerySet
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.helpers import create_user

class TestView(APIView):
	queryset = EmptyQuerySet
	permission_classes = (AllowAny,)

	def get(self, request):
		return Response([], status=200)


class UserViewSet(GenericViewSet):
	queryset = EmptyQuerySet
	permission_classes = (AllowAny,)

	def create(self, request):
		created = {'detail': 'The user has been created successfully'}
		exist = {'User already exists'}
  
		response = create_user(**request.data)
  
		data = exist if response == True else created
		return Response(data, status=status.HTTP_200_OK)
