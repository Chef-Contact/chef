from django.urls import path
from apps.host import views

urlpatterns = [
    path('becomeahost/', views.becomeahost, name='becomeahost'),
    path('index_host/', views.index_host, name='index_host'),
    path('shef_register/', views.shef_register, name='shef_register'),
]
