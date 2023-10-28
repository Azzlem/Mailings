import random

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import Blog
from clients.models import Client
from mailings.forms import MailingsForm
from mailings.models import Mailings


def index(request):
    is_active = 0
    for el in Mailings.objects.all():
        if el.status == 'Запущена':
            is_active += 1
    blog_object = Blog.objects.all().order_by('?')[:3]

    context = {
        'context_list': [
            Mailings.objects.all().count(),
            is_active,
            Client.objects.all().count(),
            blog_object,
        ]
    }
    return render(request, 'mailings/index.html', context)


class MailingsListView(ListView):
    model = Mailings
    template_name = 'mailings/mailings_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.groups.filter(name='Manager').first():
            queryset = queryset.filter(user_creator=self.request.user)

        return queryset


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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.user.email != self.object.user_creator:
            mailing_fields = [field for field in form.fields.keys()]
            for field in mailing_fields:
                if not self.request.user.has_perm(f'mailings.set_{field}'):
                    del form.fields[field]
        return form

    def get_success_url(self):
        return reverse('mailings:mailings_list')


class MailingsDetailView(DetailView):
    model = Mailings
    template_name = 'mailings/mailings_detail.html'


class MailingsDeleteView(DeleteView):
    model = Mailings

    def get_success_url(self):
        return reverse('mailings:mailings_list')
