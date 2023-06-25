from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('Registration/',views.Registration),
    path('Login/',views.Login),
]
