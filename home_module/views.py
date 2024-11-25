from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .models import Product
from django.shortcuts import render, redirect
from django.utils.translation import activate, get_language


from django.shortcuts import render
from django.utils.translation import gettext as _


# def index(request):
#     # Get the selected language from the GET parameters
#     selected_language = request.GET.get('language', None)
#
#     if selected_language:
#         # Activate the selected language
#         activate(selected_language)
#         # request.session['LANGUAGE_SESSION_KEY'] = selected_language
#         return redirect('index-page')  # Redirect to the home page to reflect the change
#
#     # Get the current language
#     current_language = get_language()
#
#     products = Product.objects.all()
#     return render(request, 'home_module/index2.html', {
#         'data': _('hello world!!'),
#         'products': products,
#         'selected_language': current_language,  # Pass the current language to the template
#     })

# ****it works too but next one is better

def index(request):
    products = Product.objects.all()

    context = {
        'data': _('hello world!!'),
        'products': products,
        'selected_language': request.LANGUAGE_CODE,  # This gets the current language
    }

    return render(request, 'home_module/index2.html', context)




