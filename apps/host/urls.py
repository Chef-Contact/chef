from django.urls import path
from apps.host import views

urlpatterns = [
    path('becomeahost/', views.becomeahost, name='becomeahost'),
    path('make_event/', views.make_event, name='make_event'),
    path('events/', views.events, name='events'),
    path('event_detail/<int:id>/', views.event_detail, name="event_detail"),
]
