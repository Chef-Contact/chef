from django.contrib import admin
from .models import *

# Register your models here.

class QuestionsInline(admin.TabularInline):
    model = Questions
    extra = 1

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', )
    search_fields = ('title', )
    inlines = [QuestionsInline]