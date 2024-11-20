"""
URL configuration for Salus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('wp-salus-admin/defender/', include('defender.urls')), # defender admin

    # Admin page honeypot

    path('admin/', include('admin_honeypot.urls')),

    #Our actual admin page
    
    path('wp-salus-admin/', admin.site.urls),
    
    
    path('rosetta/', include('rosetta.urls')),
    
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]

urlpatterns += i18n_patterns(
    path('', include("appSalus.urls")),
    prefix_default_language=False 
    # Add other i18n URL patterns for your app here
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



