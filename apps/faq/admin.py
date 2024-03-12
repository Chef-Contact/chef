from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

# Register your models here.

class QuestionsInline(admin.TabularInline):
    model = Questions
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('Russian Version', {
                'fields': ('question_ru', 'answer_ru',),
            }),
            ('English Version', {
                'fields': ('question_en', 'answer_en',),
            }),
            )
        return fieldsets

class FAQAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {
            'fields': ('title_ru', 'description_ru'),
        }),
        ('English Version', {
            'fields': ('title_en', 'description_en'),
        }),
    )
    inlines = [QuestionsInline]

admin.site.register(FAQ, FAQAdmin)

# @admin.register(FAQ)
# class FAQAdmin(admin.ModelAdmin):
#     list_display = ('title', )
#     list_filter = ('title', )
#     search_fields = ('title', )
#     inlines = [QuestionsInline]