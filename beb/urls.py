from django.urls import path
from beb import views

urlpatterns = [
    path("valentines", views.valentine_template, name="valentines"),
    path("happy-birthday", views.birthday, name="birthday"),
    path("switch-proposal", views.switch_proposal, name="switch-proposal"),
]
