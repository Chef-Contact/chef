from django.contrib import admin
from apps.base import models 

class BecomeInline(admin.TabularInline):
    model = models.Become
    extra = 1

class PerfectAdmin(admin.TabularInline):
    model = models.Perfect
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

class BenefistAdmin(admin.TabularInline):
    model = models.Benefist
    extra = 1


@admin.register(models.Become)
class BecomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ("title",)
    search_fields = ('title', )
    inlines = [
        BecomeInline, PerfectAdmin, WorkAdmin, FeaturedAdmin,
        CookingAdmin, BenefistAdmin
               ]

admin.site.register(models.Settings)
admin.site.register(models.Policies)
admin.site.register(models.Privacy)

class InsuranceInline(admin.TabularInline):
    model = models.InsuranceObjects
    extra = 1

class TrustInline(admin.TabularInline):
    model = models.TrustSafetyObjects
    extra = 1
@admin.register(models.TrustSafety)
class TrustSafetyAdmin(admin.ModelAdmin):
    list_display = ('title_banner', )
    list_filter = ('title_banner', )
    search_fields = ('title_banner', )
    inlines = [InsuranceInline, TrustInline]
