# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models.products import (
    Product,
)


class ProductCreateView(CreateView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product


class ProductListView(ListView):
    model = Product
