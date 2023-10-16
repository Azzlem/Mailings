from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mailings.forms import MailingsForm, MessageForm
from mailings.models import Mailings, Message


def index(request):
    return render(request, 'mailings/base.html')


class MailingsListView(ListView):
    model = Mailings
    template_name = 'mailings/mailings_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        return context_data


class MailingsCreateView(CreateView):
    model = Mailings
    form_class = MailingsForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_creator = self.request.user.email
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailings:mailings_list')


class MailingsUpdateView(UpdateView):
    model = Mailings
    form_class = MailingsForm

    def get_success_url(self):
        return reverse('mailings:mailings_list')


class MailingsDetailView(DetailView):
    model = Mailings
    template_name = 'mailings/mailings_detail.html'


class MailingsDeleteView(DeleteView):
    model = Mailings

    def get_success_url(self):
        return reverse('mailings:mailings_list')
