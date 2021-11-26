from django.urls import path
from django.contrib import admin
from .views import DemoView


urlpatterns = [
    path('list/', DemoView),
]
