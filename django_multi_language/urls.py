from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('rosetta/', include('rosetta.urls')),
    prefix_default_language=False
    # if it is False it doesn't display default language in url==> # website.com/en/==>website.com
)