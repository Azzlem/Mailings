from django.contrib import admin

from mailings.models import Message


@admin.register(Message)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", 'name')
