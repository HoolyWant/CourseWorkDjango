from datetime import datetime
from mail.services.send_mail import mail_seller
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class MessageDetail(DetailView):
    model = MessagesForDistribution


class MaillingCreate(CreateView):
    model = MailDistributionSettings
    form_class = MaillingForm
    success_url = reverse_lazy('mail:mailling_list')

    def form_valid(self, form):
        date_start = datetime.strptime(str(form.instance.date_start)[:19], '%Y-%m-%d %H:%M:%S')
        date_finish = datetime.strptime(str(form.instance.date_finish)[:19], '%Y-%m-%d %H:%M:%S')
        # if form.instance.distribution_status == 'created':
        if date_start <= datetime.now() <= date_finish:
            message_id = form.instance.message_id
            message = MessagesForDistribution.objects.get(pk=message_id)
            while True:
                count = 1
                client = Client.objects.get(pk=count).__dict__
                mail_seller(client, message)
        return super().form_valid(form)



class MaillingDetail(DetailView):
    model = MailDistributionSettings


class MaillingList(ListView):  # просмотр списка рассылок
    model = MailDistributionSettings

class MaillingDelete(DeleteView):



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


def home(request):
    return render(request, 'mail/home.html')


