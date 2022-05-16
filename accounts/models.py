from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
	"""Profile model.
	Proxy model that extends the base data with other
	information.
	"""
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	age = models.IntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True, editable=False)
	date_modified = models.DateTimeField(null=True)

	def __str__(self):
		"""Return username."""
		return '{}'.format(self.user.username)
