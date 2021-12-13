from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = 'owner', 'name', 'admin_preview'
    list_display_links = 'name',
    search_fields = 'owner',


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name', 'display', 'admin_preview')
    list_display_links = ('name',)
    filter_fields = ('display')
    search_fields = ('name',)
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'admin_preview',
        'seller',
        'present',
        'price'
    )
    list_display_links = 'title',
    search_fields = ('seller__owner', )
    list_filter = (
        ('category', TreeRelatedFieldListFilter),
    )
    filter_horizontal = (
        'attachments',
    )


admin.site.register(Attachment)
