from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from mail.forms import MessagesForm, MaillingForm, ClientForm
from mail.models import MessagesForDistribution, MailDistributionSettings, Logs, Client


class MessagesList(ListView):  # просмотр списка рассылок
    model = MessagesForDistribution


class MessageCreate(CreateView):
    model = MessagesForDistribution
    form_class = MessagesForm
    success_url = reverse_lazy('mail:messages_list')


class MessageEdit(UpdateView):
    model = MessagesForDistribution
    form_class = MessagesForm
    success_url = reverse_lazy('mail:messages_list')


class MaillingCreate(CreateView):
    model = MailDistributionSettings
    form_class = MaillingForm
    success_url = reverse_lazy('mail:mailling_list')


class MaillingList(ListView):  # просмотр списка рассылок
    model = MailDistributionSettings


class MaillingEdit(UpdateView):
    model = MailDistributionSettings
    form_class = MaillingForm
    success_url = reverse_lazy('mail:mailling_list')


class ClientCreate(CreateView):  # создание клиента
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')


class ClientEdit(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')


class ClientsList(ListView):  # просмотр списка клиентов
    model = Client


class LogDetail(DetailView):  # просмотр логов
    model = Logs

