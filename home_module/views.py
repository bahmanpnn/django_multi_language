from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'data': _('hello world!!'),
        'products': products
    }

    return render(request, 'home_module/index.html', context)
