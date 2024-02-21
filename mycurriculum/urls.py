"""
URL configuration for mycurriculum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .import views

urlpatterns = [
    # path('fakeadmin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('horenadmin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cvitae/', include('cvitae.urls')),
     path('current_year', views.current_year, name='current_year'),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "My Curriculum Vitae"
admin.site.site_header = "My Curriculum Vitae"
admin.site.site_title = "My Curriculum Vitae"

