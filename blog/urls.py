# this is the url for blog application 
from django.contrib import admin
from django.urls import path, include
from django.views.generics import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]
