from modeltranslation.translator import register, TranslationOptions
from .models import About

@register(About)
class CargoTranslationOptions(TranslationOptions):
    fields = ('title_banner', 'description_banner', 'image_banner', 'title_about', \
              'title_about2', 'title_about3', 'description_about', 'description_about2', 'description_about3')