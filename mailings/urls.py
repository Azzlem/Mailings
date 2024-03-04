from django.urls import path
from django.views.decorators.cache import cache_page

from clients.views import LogMailingsView
from mailings.apps import MainConfig
from mailings.views import index, MailingsListView, MailingsCreateView, MailingsUpdateView, MailingsDetailView, \
    MailingsDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(index), name='index'),
    path('mailings_list/', cache_page(60)(MailingsListView.as_view()), name='mailings_list'),
    path('mailings_create/', MailingsCreateView.as_view(), name='mailings_create'),
    path('mailings_update/<int:pk>', MailingsUpdateView.as_view(), name='mailings_update'),
    path('mailings_detail/<int:pk>', MailingsDetailView.as_view(), name='mailings_detail'),
    path('mailings_delete/<int:pk>', MailingsDeleteView.as_view(), name='mailings_delete'),
    path('log_mailings/', cache_page(60)(LogMailingsView.as_view()), name='log_mailings'),

]
