from django.urls import path, include
from secondapp import views

urlpatterns = [
    path('main/', views.main),
    path('show/', views.show),
]