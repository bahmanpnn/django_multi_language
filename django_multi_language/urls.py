from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('set_language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('rosetta/', include('rosetta.urls')),
    prefix_default_language=True
    # if it is False it doesn't display default language in url==> # website.com/en/==>website.com
)
