from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    context = {
        'data': _('hello world!!')
    }

    return render(request, 'home_module/index.html', context)
