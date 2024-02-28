from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(BecomeaHost)
class BecomeaHostTranslationOptions(TranslationOptions):
    fields = (
        'title', 'descriptions', 'image', 'title2', 'title3', 'title4', 
        'descriptions2', 'title5', 'descriptions3', 'title6', 
        'descriptions4', 'title_end', 'image_end'
    )

@register(Free)
class FreeTranslationOptions(TranslationOptions):
    fields = ('title', 'descritions', 'icon')

@register(Guests)
class GuestsTranslationOptions(TranslationOptions):
    fields = ('title', 'descritions', 'icon')

@register(Receive)
class ReceiveTranslationOptions(TranslationOptions):
    fields = ('title', 'descritions', 'icon')

@register(BecomeEnd)
class BecomeEndTranslationOptions(TranslationOptions):
    fields = ('title', 'descritions', 'icon')

@register(BlogActive)
class BlogActiveTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image')

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'image')

@register(Host)
class HostTranslationOptions(TranslationOptions):
    fields = (
        'title_descriptions',
        'button',
        'button_2',
        'button_3',
        'question_1',
        'question_2',
        'question_3',
        'question_4',
        'question_5',
        'question_6',
        'question_7',
        'question_8',
        'question_9',
        'question_10',
        'question_11',
        'question_12',
        'question_13',
        'question_14',
        'question_15',
        'question_16',
        'question_17',
        'question_18',
    )

