from django import forms
from .models import Product


class ProductsForm(forms.Form):
    model = Product
    name = forms.CharField(max_length=30, required=True)
    image = forms.ImageField(upload_to='images/', required=True)
    description = forms.CharField(max_length=300, required=True)
    category = forms.CharField(max_length=3)
    date_posted = forms.DateTimeField(auto_now_add=True, blank=True)
    start_price = forms.DecimalField(max_digits=8, decimal_places=4, required=True)
    buy_now_price = forms.DecimalField(max_digits=8, decimal_places=4, required=True)


class ReviewForm(forms.Form):
    rating = forms.IntegerField(required=True, min_value=1, max_value=5)
    comment = forms.CharField(required=True, widget=forms.Textarea)
