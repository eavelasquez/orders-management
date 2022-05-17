"""WebAppWithDjango URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.urls import path

from WebAppWithDjango import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
