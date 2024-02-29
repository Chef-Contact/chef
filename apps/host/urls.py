from django.urls import path
from apps.host import views

urlpatterns = [
    path('becomeahost/', views.becomeahost, name='becomeahost'),
    path('index_step1/', views.index_step1, name='index_event'),
    path('index_step2/', views.index_step2, name='index_step2'),
]
