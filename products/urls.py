from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductsList

app_name = 'products'

urlpatterns = [
        path('productlist/', ProductsList.as_view(), name='products_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
