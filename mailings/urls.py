from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import index

app_name = MailingsConfig.name

urlpatterns = [
    path('', index, name='index'),

]
