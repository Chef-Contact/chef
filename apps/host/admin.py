from django.contrib import admin
from apps.host import models 
from apps.host.models import PriceFood
# Register your models here.

class PriceFoodInline(admin.TabularInline):
    model =PriceFood
    extra = 1


admin.site.register(models.BecomeaHost)
admin.site.register(models.Free)
admin.site.register(models.Guests)
admin.site.register(models.Receive)
admin.site.register(models.BecomeEnd)
admin.site.register(models.Blog)
admin.site.register(models.BlogActive)