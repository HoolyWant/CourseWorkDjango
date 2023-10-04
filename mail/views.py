from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

from mail.services.send_mail import mail_seller
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
        self.object.user = self.request.user
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
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    # def form_valid(self, form):
    #     date_start = datetime.strptime(str(form.instance.date_start)[:4], '%H:%M')
    #     date_finish = datetime.strptime(str(form.instance.date_finish)[:4], '%H:%M')
    #     time_now = datetime.strptime(datetime.now().strftime('%H:%M'), '%H:%M')
    #     if date_start <= time_now <= date_finish:
    #             client_id = form.instance.client_id
    #             client = Client.objects.get(pk=client_id)
    #             message_id = MailDistributionSettings.objects.get('message_id')
    #             message = MessagesForDistribution.objects.get(pk=message_id).__dict__
    #             mail_seller(client, message)
    #     return super().form_valid(form)


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


class ClientCreate(LoginRequiredMixin, CreateView):  # создание клиента
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')
    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
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
    return render(request, 'mail/home.html')
