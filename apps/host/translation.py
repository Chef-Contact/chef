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
