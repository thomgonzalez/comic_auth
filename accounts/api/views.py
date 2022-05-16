
from django.db.models.query import EmptyQuerySet
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated


class TestView(APIView):
	queryset = EmptyQuerySet
	permission_classes = (AllowAny,)

	def get(self, request):
		return Response([], status=200)