"""WebAppWithDjango URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from WebAppWithDjango import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
