from django.contrib import admin
from .models import home_contact, Directors


@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'modified_date')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(home_contact)
class HomeContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')


