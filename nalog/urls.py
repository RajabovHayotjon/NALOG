from django.urls import path
from nalog.views import home_view, about_view


app_name = 'nalog'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),

]