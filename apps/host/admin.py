from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.host import models 

class BecomeaHostAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('image', 'image_end')}),
        ('Russian Version', {'fields': (
            'title_ru', 'descriptions_ru', 'title2_ru', 'title3_ru', 'title4_ru',
            'descriptions2_ru', 'title5_ru', 'descriptions3_ru', 'title6_ru',
            'descriptions4_ru', 'title_end_ru'
        )}),
        ('English Version', {'fields': (
            'title_en', 'descriptions_en', 'title2_en', 'title3_en', 'title4_en',
            'descriptions2_en', 'title5_en', 'descriptions3_en', 'title6_en',
            'descriptions4_en', 'title_end_en'
        )}),
    )
admin.site.register(models.BecomeaHost, BecomeaHostAdmin)

class FreeAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('icon',)}),
        ('Russian Version', {'fields': ('title_ru', 'descritions_ru')}),
        ('English Version', {'fields': ('title_en', 'descritions_en')}),
    )
admin.site.register(models.Free, FreeAdmin)

class GuestsAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('icon',)}),
        ('Russian Version', {'fields': ('title_ru', 'descritions_ru')}),
        ('English Version', {'fields': ('title_en', 'descritions_en')}),
    )
admin.site.register(models.Guests, GuestsAdmin)

class ReceiveAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('icon',)}),
        ('Russian Version', {'fields': ('title_ru', 'descritions_ru')}),
        ('English Version', {'fields': ('title_en', 'descritions_en')}),
    )
admin.site.register(models.Receive, ReceiveAdmin)

class BecomeEndAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('icon',)}),
        ('Russian Version', {'fields': ('title_ru', 'descritions_ru')}),
        ('English Version', {'fields': ('title_en', 'descritions_en')}),
    )
admin.site.register(models.BecomeEnd, BecomeEndAdmin)

class BlogAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('image',)}),
        ('Russian Version', {'fields': ('title_ru', 'descriptions_ru',)}),
        ('English Version', {'fields': ('title_en', 'descriptions_en',)}),
    )
admin.site.register(models.Blog, BlogAdmin)

class BlogActiveAdmin(TranslationAdmin):
    fieldsets = (
        ('General', {'fields': ('image',)}),
        ('Russian Version', {'fields': ('title_ru', 'descriptions_ru',)}),
        ('English Version', {'fields': ('title_en', 'descriptions_en',)}),
    )
admin.site.register(models.BlogActive, BlogActiveAdmin)
class HostAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {'fields': ('title_descriptions_ru',
        'steps_ru',
        'button_ru',
        'button_2_ru',
        'button_3_ru',
        'question_1_ru',
        'question_2_ru',
        'question_3_ru',
        'question_4_ru',
        'question_5_ru',
        'question_6_ru',
        'question_7_ru',
        'question_8_ru',)}),
        ('English Version', {'fields': ('title_descriptions_en',
        'steps_en',
        'button_en',
        'button_2_en',
        'button_3_en',
        'question_1_en',
        'question_2_en',
        'question_3_en',
        'question_4_en',
        'question_5_en',
        'question_6_en',
        'question_7_en',
        'question_8_en',)}),
    )
admin.site.register(models.Host, HostAdmin)