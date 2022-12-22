from django.urls import path

from charityfinderapp import views

urlpatterns = [
    path('charity', views.charity),

]
