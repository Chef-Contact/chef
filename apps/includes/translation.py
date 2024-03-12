from modeltranslation.translator import register, TranslationOptions

from .models import *

@register(HeaderTranslationModel)
class HeaderTranslationOptions(TranslationOptions):
    fields = (
        'language_button', 'become_a_chef_button', 'sign_in', 'login', 'messages',
        'profile', 'account_settings', 'logout', 'new_event', 'events_in_progress',
        'performances', 'demands', 'payments_in', 'reservations', 'payments_out', 'espace_home'
    )

@register(FooterTranslationModel)
class FooterTranslationOption(TranslationOptions):
    fields = ('about', 'policies', 'privacy', 'contests', 'trustandsafety', 'press', 'faq',
               'contact_us', 'howdoes', 'becomeahost', 'hospitality', 'specific_diets',
                 'explore', 'host', 'social_media')