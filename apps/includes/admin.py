from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

# Register your models here.
class HeaderTranslationAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {'fields': ('language_button_ru', 'become_a_chef_button_ru', 'sign_in_ru', 'login_ru', 'messages_ru',
                                 'profile_ru', 'account_settings_ru', 'logout_ru', 'new_event_ru', 'events_in_progress_ru',
                                 'performances_ru', 'demands_ru', 'payments_in_ru', 'reservations_ru', 'payments_out_ru', 'espace_home_ru')}),  # Добавьте поля для русской версии, если они отличаются
        ('English Version', {'fields': ('language_button_en', 'become_a_chef_button_en', 'sign_in_en', 'login_en', 'messages_en',
                                 'profile_en', 'account_settings_en', 'logout_en', 'new_event_en', 'events_in_progress_en',
                                 'performances_en', 'demands_en', 'payments_in_en', 'reservations_en', 'payments_out_en', 'espace_home_en')}),  # Добавьте поля для английской версии, если они отличаются
    )
admin.site.register(HeaderTranslationModel, HeaderTranslationAdmin)
class FooterTranslationAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {'fields': ('about_ru', 'policies_ru', 'privacy_ru', 'contests_ru', 'trustandsafety_ru', 'press_ru', 'faq_ru', 'contact_us_ru',
        'howdoes_ru', 'becomeahost_ru', 'hospitality_ru', 'specific_diets_ru', 'explore_ru', 'host_ru', 'social_media_ru' )}),  # Добавьте поля для русской версии, если они отличаются
        ('English Version', {'fields': ('about_en', 'policies_en', 'privacy_en', 'contests_en', 'trustandsafety_en', 'press_en', 'faq_en', 'contact_us_en',
        'howdoes_en', 'becomeahost_en', 'hospitality_en', 'specific_diets_en', 'explore_en', 'host_en', 'social_media_en' )}),  # Добавьте поля для английской версии, если они отличаются
    )
admin.site.register(FooterTranslationModel, FooterTranslationAdmin)