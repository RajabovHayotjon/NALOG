from django.contrib import admin
from .models import RegisterUs, LoginUs




@admin.register(RegisterUs)
class RegisterUSAdmin(admin.ModelAdmin):
    list_display = ('user',  'password', 'password2')
    list_filter = ('password', 'password2')

@admin.register(LoginUs)
class LoginUsAdmin(admin.ModelAdmin):
    list_display = ('user', 'password')
    search_fields = ('username', 'password')