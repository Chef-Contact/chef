from django.urls import path
from apps.host import views

urlpatterns = [
    path('becomeahost/', views.becomeahost, name='becomeahost'),
    path('index_event/', views.index_event, name='index_event'),
    path('make_event/', views.make_event, name='make_event'),
    path('event_detail/<int:id>/', views.event_detail, name="event_detail"),
]
