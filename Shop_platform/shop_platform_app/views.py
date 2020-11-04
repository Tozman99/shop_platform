from django.shortcuts import render
from shops.models import Product

# Create your views here.


def home_view(request):

	products = Product.objects.all()
	sports = []
	health = []
	tech = []

	for product in products:

		if len(sports) < 3 and product.category == "Sport":
			
			sports.append(product)

		elif len(health) < 3 and product.category == "Health":

			health.append(product)

		elif len(tech) < 3 and product.category == "Tech":

			tech.append(product)

	return render(request, "homepage.html", {"sport_products": sports, "health_products": health, "tech_products": tech})
