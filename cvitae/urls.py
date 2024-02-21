from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('email_compose/', views.email_compose, name='email_compose'),
    path('profile/', views.profile, name='profile'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/', views.project, name='project'),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)