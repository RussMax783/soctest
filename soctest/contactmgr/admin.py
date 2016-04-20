from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'full_address')


admin.site.register(Contact, ContactAdmin)
