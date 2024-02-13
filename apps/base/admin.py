from django.contrib import admin
from apps.base import models
from apps.host.admin import PriceFoodInline


class BecomeInline(admin.TabularInline):
    model = models.Become
    extra = 1

class WorkAdmin(admin.TabularInline):
    model = models.Work
    extra = 1

class FeaturedAdmin(admin.TabularInline):
    model = models.Featured
    extra = 1

class CookingAdmin(admin.TabularInline):
    model = models.Cooking
    extra = 1

class CookingActiveAdmin(admin.TabularInline):
    model = models.CookingActive
    extra = 1

class BenefistAdmin(admin.TabularInline):
    model = models.Benefist
    extra = 1

class BecomeActiveAdmin(admin.TabularInline):
    model = models.BecomeActive
    extra = 1


@admin.register(models.Become)
class BecomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ("title",)
    search_fields = ('title', )
    inlines = [
        BecomeInline, WorkAdmin, FeaturedAdmin,
        CookingAdmin,CookingActiveAdmin, BenefistAdmin, BecomeActiveAdmin
               ]


class PerfectInline(admin.TabularInline):
    model = models.PerfectActive
    extra = 1

@admin.register(models.Perfect)
class PerfectAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ("title", )
    search_fields = ('title', )
    inlines = [PerfectInline, PriceFoodInline]



class HowitworksObjectInline(admin.TabularInline):
    model = models.HowitworksObject
    extra = 1

class GuestsHostsInline(admin.TabularInline):
    model = models.GuestsHosts
    extra = 1


@admin.register(models.Howitworks)
class HotiworksAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ("title", )
    search_fields = ('title', )
    inlines = [HowitworksObjectInline, GuestsHostsInline]


admin.site.register(models.Settings)
admin.site.register(models.Policies)
admin.site.register(models.Privacy)
admin.site.register(models.Hospitaly)
admin.site.register(models.Specefic)