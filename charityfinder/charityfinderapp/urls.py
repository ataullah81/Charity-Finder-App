from django.urls import path

from charityfinder import views

urlpatterns = [
    path('cahrityform', views.charity, name='cahrityform'),

]
