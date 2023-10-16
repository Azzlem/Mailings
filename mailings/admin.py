from django.contrib import admin

from mailings.models import Message, Mailings, Client


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("pk", 'name')


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'periodicity',
        'status',
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'email',
    )
