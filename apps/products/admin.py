from django.contrib import admin
from apps.products.models import Category, Kind, Product, ProductRequest
# Register your models here.
admin.site.register(Category)
admin.site.register(Kind)
admin.site.register(Product)
admin.site.register(ProductRequest)