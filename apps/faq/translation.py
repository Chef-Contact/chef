from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(FAQ)
class FAQTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Questions)
class QuestionsTranslationOption(TranslationOptions):
    fields = ('question', 'answer')