from django.urls import path, reverse_lazy
from account.views import account_login, account_register , logout_view

app_name = 'account'

urlpatterns = [
    path('account_login/', account_login, name='account_login'),
    path('account_register/', account_register, name='account_register'),
    path('logout/', logout_view, name='logout'),
]