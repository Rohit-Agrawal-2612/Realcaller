from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('search/', views.search),
    path('spam/', views.spam),
    path('contacts/',views.contacts)
]