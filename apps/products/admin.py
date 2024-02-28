from django.contrib import admin
from apps.products.models import Category, Kind
# Register your models here.
admin.site.register(Category)
admin.site.register(Kind)