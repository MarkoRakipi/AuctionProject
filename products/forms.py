from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'category',
            'start_price',
            'buy_now_price',
        ]


class ReviewForm(forms.Form):
    rating = forms.IntegerField(required=True, min_value=1, max_value=5)
    comment = forms.CharField(required=True, widget=forms.Textarea)
