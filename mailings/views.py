from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from mailings.forms import MailingsForm
from mailings.models import Mailings


def index(request):
    return render(request, 'mailings/base.html')


class MailingsListView(ListView):
    model = Mailings
    template_name = 'mailings/mailings_list.html'


class MailingsCreateView(CreateView):
    model = Mailings
    form_class = MailingsForm

    def get_success_url(self):
        return reverse('mailings:mailings_list')


class MailingsUpdateView(UpdateView):
    model = Mailings
    form_class = MailingsForm

    def get_success_url(self):
        return reverse('mailings:mailings_list')