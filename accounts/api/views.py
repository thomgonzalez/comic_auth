
from django.db.models.query import EmptyQuerySet
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, RegisterSerializer


from django.contrib.auth.models import User
from accounts.helpers import create_user

class TestView(APIView):
	queryset = EmptyQuerySet
	permission_classes = (AllowAny,)

	def get(self, request):
		return Response([], status=200)


class UserViewSet(GenericViewSet):
	queryset = User.objects.all()
	serializer_class =  RegisterSerializer
	permission_classes = (AllowAny,)

	def create(self, request):
		created = {'detail': 'The user has been created successfully'}
		exist = {'User already exists'}
  
		serializer = RegisterSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
  
		response = create_user(**request.data)
  
		data = exist if response == True else created
		return Response(data, status=status.HTTP_200_OK)
