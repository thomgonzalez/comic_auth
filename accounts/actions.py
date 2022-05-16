from django.contrib.auth.models import User
from accounts.models import Profile


class UserAction(object):

	def create(self, **kwargs):
		instance = User(**kwargs)
		instance.save()
		return instance

	def get(self, **kwargs):
		try:
			return User.objects.get(**kwargs)
		except User.DoesNotExist:
			return None

	def filter(self, **kwargs):
		try:
			return User.objects.filter(**kwargs)
		except User.DoesNotExist:
			return None

class PerfileAction(object):

	def create(self, **kwargs):
		instance = Profile(**kwargs)
		instance.save()
		return instance