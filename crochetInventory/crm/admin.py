from django.contrib import admin
from .models import CrochetHook, Yarn, Gift


class CrochetHookList(admin.ModelAdmin):
    list_display = ('crochetHook_size', 'count', 'material')
    list_filter = ('crochetHook_size', 'material')
    search_fields = ('crochetHook_size',)
    ordering = ['crochetHook_size']


class YarnList(admin.ModelAdmin):
    list_display = ('crochetHook_size', 'yarn_color', 'yarn_texture', 'yarn_amount')
    list_filter = ('crochetHook_size', 'yarn_color')
    search_fields = ('crochetHook_size',)
    ordering = ['crochetHook_size']


class GiftList(admin.ModelAdmin):
    list_display = ('crochetHook_size', 'yarn_color', 'recipient_name', 'gift_size')
    list_filter = ('crochetHook_size', 'recipient_name')
    search_fields = ('crochetHook_size',)
    ordering = ['crochetHook_size']


admin.site.register(CrochetHook, CrochetHookList)
admin.site.register(Yarn, YarnList)
admin.site.register(Gift, GiftList)
