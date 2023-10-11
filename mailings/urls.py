from django.urls import path

from mailings.apps import MainConfig
from mailings.views import index, MailingsListView, MailingsCreateView, MailingsUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('mailings_list/', MailingsListView.as_view(), name='mailings_list'),
    path('mailings_create/', MailingsCreateView.as_view(), name='mailings_create'),
    path('mailings_update/<int:pk>', MailingsUpdateView.as_view(), name='mailings_update'),

]
