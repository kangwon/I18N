from django.contrib import admin

from app.models import Key, Translation


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = list_display


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'key_id', 'locale', 'value',)
    list_display_links = list_display
