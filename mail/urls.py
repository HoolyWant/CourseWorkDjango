from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mail.apps import MailConfig
from mail.views import MessagesList, MessageCreate, ClientCreate, ClientsList, \
    MaillingCreate, MaillingList, MaillingEdit, ClientEdit, MessageEdit, LogDetail

app_name = MailConfig.name

urlpatterns = [
    path('messages', MessagesList.as_view(template_name='mail/messages_list.html'), name='messages_list'),
    path('messages/<int:pk>', MessageEdit.as_view(template_name='mail/message_form.html'), name='messages_view'),
    path('messages/create', MessageCreate.as_view(template_name='mail/message_form.html'), name='message_create'),
    path('clients', ClientsList.as_view(template_name='mail/clients_list.html'), name='clients_list'),
    path('clients/<int:pk>', ClientEdit.as_view(template_name='mail/client_form.html'), name='client_edit'),
    path('clients/create', ClientCreate.as_view(template_name='mail/client_form.html'), name='client_create'),
    path('mailling/create', MaillingCreate.as_view(template_name='mail/mailling_form.html'), name='mailling_create'),
    path('mailling/<int:pk>', MaillingEdit.as_view(template_name='mail/mailling_form.html'), name='mailling_edit'),
    path('mailling', MaillingList.as_view(template_name='mail/mailling_list.html'), name='mailling_list'),
    path('logs', LogDetail.as_view(template_name='mail/log_form.html'), name='logs'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
