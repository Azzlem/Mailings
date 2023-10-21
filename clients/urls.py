from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDetailView, ClientsDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('clients_create/', ClientsCreateView.as_view(), name='clients_create'),
    path('clients_update/<int:pk>', ClientsUpdateView.as_view(), name='clients_update'),
    path('clients_detail/<int:pk>', ClientsDetailView.as_view(), name='clients_detail'),
    path('clients_delete/<int:pk>', ClientsDeleteView.as_view(), name='clients_delete'),

]