from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('air/', air, name='air'),
    path('contacts', contacts, name='contacts'),
    path('eco-report/', eco_report, name='eco_report'),
    path('ecology/', ecology, name='ecology'),
    path('refuse/', refuse, name='refuse'),
    path('water/', water, name='water'),
]