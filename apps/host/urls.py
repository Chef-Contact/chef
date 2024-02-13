from django.urls import path
from apps.host import views

urlpatterns = [
    path('becomeahost/', views.becomeahost, name='becomeahost'),
]
