from django.urls import path
from . import views



urlpatterns =[
    path('email_compose/', views.email_compose, name='email_compose'),
    path('profile/', views.profile, name='profile'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/', views.project, name='project'),
]