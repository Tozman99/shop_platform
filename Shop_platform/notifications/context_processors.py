from .models import Notification
from users.models import Profile
from django.shortcuts import get_object_or_404

def notif_bell(request):

	if request.user.is_authenticated:

		try:

			profile = get_object_or_404(Profile, user=request.user)
			notifications = Notification.object.all().filter(user=profile)

			return {"notifications":notifications}

		except:

			return {"notifications":False}

		return {"notifications":False}
