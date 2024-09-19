from django.contrib import admin
from .models import ContactUs, Practice


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date', 'modified_date')
    search_fields = ('name',)
    list_filter = ('email',)


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'modified_date')
    search_fields = ('title',)
    list_filter = ('title',)
