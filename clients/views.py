from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from clients.models import Client
from clients.forms import ClientsForm
from mailings.models import LogMailings


class ClientsListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        return context_data


class ClientsCreateView(CreateView):
    model = Client
    form_class = ClientsForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_creator = self.request.user.email
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Client
    form_class = ClientsForm

    def get_success_url(self):
        return reverse('clients:clients_list')


class ClientsDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'


class ClientsDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        return reverse('clients:clients_list')


class LogMailingsView(ListView):
    model = LogMailings
    template_name = 'mailings/log_mailings_list.html'
