from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Blog
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from mail.forms import MessagesForm, MaillingForm, ClientForm
from mail.models import MessagesForDistribution, MailDistributionSettings, Logs, Client


class MessagesList(LoginRequiredMixin, ListView):  # просмотр списка рассылок
    model = MessagesForDistribution


class MessageCreate(LoginRequiredMixin, CreateView):
    model = MessagesForDistribution
    form_class = MessagesForm
    success_url = reverse_lazy('mail:messages_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)



class MessageEdit(LoginRequiredMixin, UpdateView):
    model = MessagesForDistribution
    form_class = MessagesForm
    success_url = reverse_lazy('mail:messages_list')


class MessageDetail(DetailView):
    model = MessagesForDistribution


class MaillingCreate(LoginRequiredMixin, CreateView):
    model = MailDistributionSettings
    form_class = MaillingForm
    success_url = reverse_lazy('mail:mailling_list')
    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class MaillingDetail(DetailView):
    model = MailDistributionSettings


class MaillingList(LoginRequiredMixin, ListView):  # просмотр списка рассылок
    model = MailDistributionSettings


class MaillingDelete(DeleteView):
    model = MailDistributionSettings
    success_url = reverse_lazy('mail:mailling_list')


class MaillingEdit(UpdateView):
    model = MailDistributionSettings
    form_class = MaillingForm
    success_url = reverse_lazy('mail:mailling_list')

    def form_valid(self, form):
        self.object = form.save()
        if self.request.user.is_staff:
            mailing_settings = self.object
            if mailing_settings.user != self.request.user:
                mailing_settings.status = form.cleaned_data['status']

        self.object.save()

        return super().form_valid(form)


class ClientCreate(LoginRequiredMixin, CreateView):  # создание клиента
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')
    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientEdit(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')


class ClientsList(LoginRequiredMixin, ListView):  # просмотр списка клиентов
    model = Client


class LogsList(LoginRequiredMixin, ListView):  # просмотр логов
    model = Logs


def home(request):
    mailling_count = MailDistributionSettings.objects.count()
    active_mailling_count = MailDistributionSettings.objects.filter(distribution_status='started').count()
    unic_clients = MailDistributionSettings.objects.distinct().count()
    blogs = Blog.objects.order_by('?')[:3]
    context = {
        'mailling_count': mailling_count,
        'active_mailling_count': active_mailling_count,
        'unic_clients': unic_clients,
        'blogs': blogs,
    }
    return render(request, 'mail/home.html', context)


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:clients_list')


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = MessagesForDistribution
    success_url = reverse_lazy('mail:messages_list')
