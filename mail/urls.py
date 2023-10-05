from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mail.apps import MailConfig
from mail.views import MessagesList, MessageCreate, ClientCreate, ClientsList, \
    MaillingCreate, MaillingList, MaillingEdit, ClientEdit, MessageEdit, home, MessageDetail, MaillingDetail, \
    MaillingDelete, LogsList, MessageDelete, ClientDelete

app_name = MailConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('messages/', MessagesList.as_view(template_name='mail/messages_list.html'), name='messages_list'),
    path('messages/edit/<int:pk>', MessageEdit.as_view(template_name='mail/message_form.html'), name='message_edit'),
    path('messages/<int:pk>', MessageDetail.as_view(template_name='mail/message_detail.html'), name='message_view'),
    path('messages/create', MessageCreate.as_view(template_name='mail/message_form.html'), name='message_create'),
    path('messages/delete/<int:pk>', MessageDelete.as_view(template_name='mail/message_delete_confirm.html'), name='message_delete_confirm'),
    path('clients/', ClientsList.as_view(template_name='mail/clients_list.html'), name='clients_list'),
    path('clients/<int:pk>', ClientEdit.as_view(template_name='mail/client_form.html'), name='client_edit'),
    path('clients/delete/<int:pk>', ClientDelete.as_view(template_name='mail/client_confirm_delete.html'), name='client_confirm_delete'),
    path('clients/create', ClientCreate.as_view(template_name='mail/client_form.html'), name='client_create'),
    path('mailling/create', MaillingCreate.as_view(template_name='mail/mailling_form.html'), name='mailling_create'),
    path('mailling/edit/<int:pk>', MaillingEdit.as_view(template_name='mail/mailling_form.html'), name='mailling_edit'),
    path('mailling/<int:pk>', MaillingDetail.as_view(template_name='mail/mailling_detail.html'), name='mailling_detail'),
    path('mailling/', MaillingList.as_view(template_name='mail/mailling_list.html'), name='mailling_list'),
    path('mailling/delete/<int:pk>', MaillingDelete.as_view(template_name='mail/mailling_confirm_delete.html'), name='mailling_delete'),
    path('logs/', LogsList.as_view(template_name='mail/logs_list.html'), name='logs_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
