from django.urls import path
from beb import views

urlpatterns = [
    path("valentines", views.valentine_template, name="valentines")
]
