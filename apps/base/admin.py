from django.contrib import admin
# from apps.base.models import *
from modeltranslation.admin import TranslationAdmin

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
    search_fields = ('title',)
    inlines = [
        BecomeInline, WorkAdmin, FeaturedAdmin,
        CookingAdmin, CookingActiveAdmin, BenefistAdmin, BecomeActiveAdmin
    ]


class AboutAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image_banner',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_banner_ru', 'description_banner_ru', 'title_about_ru', 'title_about2_ru', 'title_about3_ru',
                'description_about_ru', 'description_about2_ru', 'description_about3_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_banner_en', 'description_banner_en', 'title_about_en', 'title_about2_en', 'title_about3_en',
                'description_about_en', 'description_about2_en', 'description_about3_en'),
        }),
    )
admin.site.register(models.About, AboutAdmin)


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

class SettingsAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'descriptions_ru', 'become_title_ru', 'become_descriptions_ru',
                'find_title_ru', 'find_descriptions_ru', 'work_title_ru', 'work_descriptions_ru', 'work_context_ru',
                'download_title_ru', 'download_descriptions_ru', 'host_title_ru', 'benefist_title_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'descriptions_en', 'become_title_en', 'become_descriptions_en',
                'find_title_en', 'find_descriptions_en', 'work_title_en', 'work_descriptions_en', 'work_context_en',
                'download_title_en', 'download_descriptions_en', 'host_title_en', 'benefist_title_en'),
        }),
    )
admin.site.register(models.Settings, SettingsAdmin)

class PoliciesAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'descriptions_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'descriptions_en'),
        }),
    )
admin.site.register(models.Policies, PoliciesAdmin)

class PrivacyAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'descriptions_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'descriptions_en'),
        }),
    )
admin.site.register(models.Privacy, PrivacyAdmin)

class RulesAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('main_image', 'image1', 'image2', 'flag1', 'flag2'),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'description_ru', 'lottery_rule_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'description_en', 'lottery_rule_en'),
        }),
    )
admin.site.register(models.Rules, RulesAdmin)


class InsuranceInline(admin.TabularInline):
    model = models.InsuranceObjects
    extra = 1


class TrustInline(admin.TabularInline):
    model = models.TrustSafetyObjects
    extra = 1


@admin.register(models.TrustSafety)
class TrustSafetyAdmin(admin.ModelAdmin):
    list_display = ('title_banner',)
    list_filter = ('title_banner',)
    search_fields = ('title_banner',)
    inlines = [InsuranceInline, TrustInline]


class PerfectActiveAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': ('title_ru',),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': ('title_en',),
        }),
    )
admin.site.register(models.PerfectActive, PerfectActiveAdmin)

class HospitalityAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {
            'fields': ('image',),
        }),
        ('Russian Version', {
            'fields': ('title_ru', 'descriptions_ru', 'quests_title_ru', 'quests_all_ru', 'quests_all2_ru', 'quests_all3_ru'),
        }),
        ('English Version', {
            'fields': ('title_en', 'descriptions_en', 'quests_title_en', 'quests_all_en', 'quests_all2_en', 'quests_all3_en'),
        }),
    )
admin.site.register(models.Hospitaly, HospitalityAdmin)

class SpecificAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {
            'fields': ('image',),
        }),
        ('Russian Version', {
            'fields': ('title_ru', 'descriptions_ru', 'title_about_diets_ru', 'center_ru', 'title_diets_ru', 'title_offered_ru', 'title_list_ru'),
        }),
        ('English Version', {
            'fields': ('title_en', 'descriptions_en', 'title_about_diets_en', 'center_en', 'title_diets_en', 'title_offered_en', 'title_list_en'),
        }),
    )
admin.site.register(models.Specefic, SpecificAdmin)
