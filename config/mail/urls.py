from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from config.mail.apps import MailConfig
from config.mail.views import MessagesList, MessageDetail, MessageCreate, ClientCreate, ClientsList, ClientDetail

app_name = MailConfig.name

urlpatterns = [
    path(''),
    path('/messages', MessagesList.as_view(), name='messages_list'),
    path('/messages/<int:pk>', MessageDetail.as_view(), name='messages_view'),
    path('/messages/create', MessageCreate.as_view(), name='message_create'),
    path('/clients', ClientsList.as_view(), name='clients_list'),
    path('/clients/<int:pk>', ClientDetail.as_view(), name='clients_view'),
    path('/clients/create', ClientCreate.as_view(), name='client_create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
