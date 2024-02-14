from django.contrib import admin
# from apps.base.models import *
from modeltranslation.admin import TranslationAdmin

from apps.base import models


# class BecomeInline(admin.TabularInline):
#     model = models.Become
#     extra = 1

#     def get_fieldsets(self, request, obj=None):
#         fieldsets = (
#             ('General', {
#                 'fields': ('image',),
#             }),
#             ('Russian Version', {
#                 'fields': ('title_ru', 'descriptions_ru',),
#             }),
#             ('English Version', {
#                 'fields': ('title_en', 'descriptions_en',),
#             }),
#             )
#         return fieldsets

class WorkAdmin(admin.TabularInline):
    model = models.Work
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('icon',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru'),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en'),
            }),
            )
        return fieldsets


class FeaturedAdmin(admin.TabularInline):
    model = models.Featured
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'locations_ru',),
            }),
            ('English Version', {
                'fields': ('title_en', 'locations_en',),
            }),
            )
        return fieldsets

class CookingAdmin(admin.TabularInline):
    model = models.Cooking
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru',),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en',),
            }),
            )
        return fieldsets

class CookingActiveAdmin(admin.TabularInline):
    model = models.CookingActive
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru', 'button_text_ru'),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en', 'button_text_en'),
            }),
            )
        return fieldsets

class BenefistAdmin(admin.TabularInline):
    model = models.Benefist
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image', 'color',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru',  'context_ru', 'button_text_ru'),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en', 'context_en', 'button_text_en'),
            }),
            )
        return fieldsets

class BecomeActiveAdmin(admin.TabularInline):
    model = models.BecomeActive
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru',),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en',),
            }),
            )
        return fieldsets


class BecomeAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('image',)}),
        ('Russian Version', {'fields': ('title_ru', 'descriptions_ru',)}),
        ('English Version', {'fields': ('title_en', 'descriptions_en',)}),
    )
    inlines = [BecomeActiveAdmin,
        WorkAdmin, FeaturedAdmin,
        CookingAdmin, CookingActiveAdmin, BenefistAdmin
    ]
admin.site.register(models.Become, BecomeAdmin)

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
    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image',),
            }),
            ('Russian Version', {
                'fields': ('title_ru',),
            }),
            ('English Version', {
                'fields': ('title_en',),
            }),
            )
        return fieldsets

class PerfectAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru',),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en',),
        }),
    )
    inlines = [PerfectInline]

admin.site.register(models.Perfect, PerfectAdmin)




class HowitworksObjectInline(admin.TabularInline):
    model = models.HowitworksObject
    extra = 1
    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('image',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru'),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en'),
            }),
            )
        return fieldsets


class GuestsHostsInline(admin.TabularInline):
    model = models.GuestsHosts
    extra = 1
    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('General', {
                'fields': ('icon',),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'descriptions_ru'),
            }),
            ('English Version', {
                'fields': ('title_en', 'descriptions_en'),
            }),
            )
        return fieldsets


class HowItWorksAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'descriptions_ru', 'title2_ru' , 'title3_ru', 'title4_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'descriptions_en', 'title2_en' , 'title3_en', 'title4_en'),
        }),
    )
    inlines = [HowitworksObjectInline, GuestsHostsInline]

admin.site.register(models.Howitworks, HowItWorksAdmin)



class SettingsAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('image',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'descriptions_ru', 'become_title_ru', 'become_descriptions_ru', 'become_button_text_ru',
                'find_title_ru', 'find_descriptions_ru', 'work_title_ru', 'work_descriptions_ru', 'work_button_text_ru',
                'download_title_ru', 'download_descriptions_ru', 'host_title_ru', 'host_button_text_ru', 'benefist_title_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'descriptions_en', 'become_title_en', 'become_descriptions_en', 'become_button_text_en',
                'find_title_en', 'find_descriptions_en', 'work_title_en', 'work_descriptions_en', 'work_button_text_en',
                'download_title_en', 'download_descriptions_en', 'host_title_en', 'host_button_text_en', 'benefist_title_en'),
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

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Russian Version', {
                'fields': ('question_ru', 'answer_ru'),
            }),
            ('English Version', {
                'fields': ('question_en', 'answer_en'),
            }),
        ]
        return fieldsets

class TrustInline(admin.TabularInline):
    model = models.TrustSafetyObjects
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('General', {
                'fields': ('icon_image', ),
            }),
            ('Russian Version', {
                'fields': ('title_ru', 'description_ru'),
            }),
            ('English Version', {
                'fields': ('title_en', 'description_en'),
            }),
        ]
        return fieldsets

class TrustSafetyObjectsAdmin(TranslationAdmin):
        fieldsets = (
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_ru', 'description_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_en', 'description_en'),
        }),
    )


class TrustSafetyAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {  # Общие поля, которые не требуют перевода или общие для всех языков
            'fields': ('background_image',),
        }),
        ('Russian Version', {  # Поля для русской версии
            'fields': (
                'title_banner_ru', 'description_banner_ru', 'insurance_title_ru', 'insurance_description_ru'),
        }),
        ('English Version', {  # Поля для английской версии
            'fields': (
                'title_banner_en', 'description_banner_en', 'insurance_title_en', 'insurance_description_en'),
        }),
    )
    inlines = [InsuranceInline, TrustInline]
admin.site.register(models.TrustSafety, TrustSafetyAdmin)


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
            'fields': ('title_ru', 'descriptions_ru', 'title_about_diets_ru', 'center_ru', 'title_diets_ru', 'title_allergens_ru', 'title_filters_ru', 'title_offered_ru', 'title_list_ru'),
        }),
        ('English Version', {
            'fields': ('title_en', 'descriptions_en', 'title_about_diets_en', 'center_en', 'title_diets_en', 'title_allergens_en', 'title_filters_en',  'title_offered_en', 'title_list_en'),
        }),
    )
admin.site.register(models.Specefic, SpecificAdmin)



admin.site.register(models.Gellary)