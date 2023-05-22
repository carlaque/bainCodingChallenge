from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("history/", history),
    path("", search),
    path("list/", ListGeneric.as_view())
]