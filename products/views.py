from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())