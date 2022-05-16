from django.db.models.query import EmptyQuerySet
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, RegisterSerializer

from django.contrib.auth.models import User
from accounts.helpers import create_user


class TestView(APIView):
	queryset = EmptyQuerySet
	permission_classes = (AllowAny,)

	def get(self, request):
		from pymongo import MongoClient
		client = MongoClient() 
		print(client)
		return Response([], status=200)


class UserViewSet(GenericViewSet):
	"""class User Register

	Args:
		GenericViewSet (class): subclassing the GenericViewSet
	"""
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = (AllowAny,)

	def create(self, request):
		"""APi User Create

		Args:
			request (obj): request data

		Returns:
			obj: reply message
		"""
		created = {'detail': 'The user has been created successfully'}
		exist = {'User already exists'}

		serializer = RegisterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		response = create_user(**request.data)

		data = exist if response == True else created
		return Response(data, status=status.HTTP_200_OK)


class LoginAuthToken(ObtainAuthToken):
	"""Class User Login Api view

	Args:
		ObtainAuthToken (class): subclassing the ObtainAuthToken
	"""

	def get_token(self, user):
		"""Create and get token

		Args:
			user (str): obj user

		Returns:
			obj: Return token model
		"""
		token, created = Token.objects.get_or_create(user=user)
		return token

	def post(self, request, *args, **kwargs):
		"""API Obtain User Data

		Args:
			request (obj): Request data

		Returns:
			obj: user data object
		"""
		data = {}
		serializer = self.serializer_class(data=request.data,
										   context={'request': request})
		is_valid = serializer.is_valid()
		if is_valid:
			user = serializer.validated_data['user']
			token = self.get_token(user=user)

			serializer = UserSerializer(user)
			data = serializer.data
			data.update({'token': str(token)})

			return Response(data, status=status.HTTP_200_OK)
		else:
			data = {
				'detail': 'Unregistered user.',
				'status': status.HTTP_404_NOT_FOUND
			}
			return Response(data, status=status.HTTP_404_NOT_FOUND)
