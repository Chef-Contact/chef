from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image', 'become_title', 'become_descriptions', 'become_button_text',
              'find_title', 'find_descriptions', 'work_title', 'work_descriptions', 'work_button_text',
              'download_title', 'download_descriptions', 'host_title', 'host_button_text', 'benefist_title')


@register(Become)
class BecomeTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image')


@register(BecomeActive)
class BecomeActiveTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image')


@register(Perfect)
class PerfectTranslationOptions(TranslationOptions):
    fields = ('title', 'image')


@register(PerfectActive)
class PerfectActiveTranslationOptions(TranslationOptions):
    fields = ('title', 'image')


@register(Work)
class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'icon')


@register(Featured)
class FeaturedTranslationOptions(TranslationOptions):
    fields = ('title', 'image', 'locations')


@register(Cooking)
class CookingTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image')


@register(CookingActive)
class CookingActiveTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image', 'button_text')


@register(Benefist)
class BenefistTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'context', 'image', 'color', 'button_text')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('last_name', 'email', 'number', 'message')


@register(Policies)
class PoliciesTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


@register(Privacy)
class PrivacyTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


@register(TrustSafety)
class TrustSafetyTranslationOptions(TranslationOptions):
    fields = ('title_banner', 'description_banner', 'background_image', 'insurance_title', 'insurance_description')


@register(TrustSafetyObjects)
class TrustSafetyObjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(InsuranceObjects)
class InsuranceObjectsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(Rules)
class RulesTranslationOptions(TranslationOptions):
    fields = ('main_image', 'title', 'description', 'image1', 'flag1', 'image2', 'flag2', 'lottery_rule')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title_banner', 'description_banner', 'image_banner', 'title_about', 'title_about2', 'title_about3',
              'description_about', 'description_about2', 'description_about3')

@register(Hospitaly)
class HospitalityTranslationOption(TranslationOptions):
    fields = ('title', 'descriptions', 'image', 'quests_title', 'quests_all', 'quests_all2', 'quests_all3')

@register(Specefic)
class SpecificTranslationOption(TranslationOptions):
    fields = ('title', 'descriptions', 'image', 'title_about_diets', 'center', 'title_diets', 'title_allergens', 'title_filters', 'title_offered', 'title_list')

@register(Howitworks)
class HowitworksTranslationOption(TranslationOptions):
    fields = ('title', 'descriptions', 'image', 'title2', 'title3', 'title4', )

@register(HowitworksObject)
class HowitworksObjectTranslationOption(TranslationOptions):
    fields = ('title', 'descriptions', 'image')

@register(GuestsHosts)
class GuestHostsTranslationObject(TranslationOptions):
    fields = ('title', 'descriptions', 'icon')
    