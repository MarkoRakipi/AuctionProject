from django.views.generic import ListView

from .models import Product


class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
