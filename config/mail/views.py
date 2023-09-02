from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from config.mail.models import MessagesForDistribution, MailDistributionSettings, Logs, Client


class MessagesList(ListView):  # просмотр списка рассылок
    model = MessagesForDistribution


class MessageDetail(DetailView):  # просмотр рассылки
    model = MessagesForDistribution


class MessageCreate(CreateView):  # создания рассылки с настройками
    model = MailDistributionSettings
    fields = ('message_theme', 'message_body',
              'date_start', 'date_finish',
              'period')
    success_url = reverse_lazy('mail:messages_list')


class ClientCreate(CreateView):  # созданиt клиента
    model = Client
    fields = ('full_name', 'contact_email', 'comment')
    success_url = reverse_lazy('mail:list')


class ClientDetail(DetailView):  # просмотра клиента
    model = Client


class ClientsList(ListView):  # просмотр списка клиентов
    model = Client


class LogDetail(DetailView):  # просмотр логов
    model = Logs
