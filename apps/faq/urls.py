from django.urls import path

from .views import *

urlpatterns = [
    path('faq/', faq, name="faq"),
    path('faq_detail/<int:id>/', faq_detail, name="faq_detail"),
]