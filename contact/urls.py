from django.urls import path
from contact.views import contact, practice_areas

app_name = 'contact'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('practice_areas/', practice_areas, name='practice_areas'),

]
