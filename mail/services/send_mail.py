from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def mail_seller(client, message):
    send_mail(message['message_theme'],
              f"Dear,{client['full_name']}. {message['message_body']}",
              EMAIL_HOST_USER,
              [client['contact_email'], ]
              )
