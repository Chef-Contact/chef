from django.contrib import admin
from apps.base import models 
# from apps.base.models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


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
    

class AboutAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image_banner',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': ('title_banner_ru', 'description_banner_ru', 'title_about_ru', 'title_about2_ru', 'title_about3_ru', 'description_about_ru', 'description_about2_ru', 'description_about3_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': ('title_banner_en', 'description_banner_en', 'title_about_en', 'title_about2_en', 'title_about3_en', 'description_about_en', 'description_about2_en', 'description_about3_en'),
        }),
    )
admin.site.register(models.About, AboutAdmin)


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
admin.site.register(models.Perfect)
admin.site.register(models.PerfectActive)
