from django.db import models
from users.models import Profile
from django.contrib.postgres.fields import JSONField
from orders.models import Order
# Create your models here.

notif_type = (

			("1", "order"),
			("2", "sell"),
			("3", "other")
			)

class Notification(models.Model):

	date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	message = models.CharField(max_length=200)
	#object = JSONField(blank=True, default=dict)
	read = models.BooleanField(default=False)
	type = models.CharField(choices=notif_type, max_length=50, default="other")

	def __str__(self):

		return f"Notification instance n_{self.pk} to {self.user}"

