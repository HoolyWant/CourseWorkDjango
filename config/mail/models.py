from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ClientService(models.Model):
    contact_email = models.CharField(max_length=100, verbose_name='контактная почта')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='ФИО', **NULLABLE)

    def __str__(self):
        return f'{self.full_name}({self.contact_email})'

    class Meta:
        verbose_name = 'клиент сервис'
        verbose_name_plural = 'клиент сервисы'


class MailDistributionSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = ((PERIOD_DAILY, 'Ежедневно'),
               (PERIOD_WEEKLY, 'Еженедельно'),
               (PERIOD_MONTHLY, 'Ещемесячно'))

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = ((STATUS_CREATED, 'Запущена'),
                (STATUS_STARTED, 'Создана'),
                (STATUS_DONE, 'Завершена'))
    date_start = models.DateTimeField(verbose_name='время начала рассылки')
    date_finish = models.DateTimeField(verbose_name='время окончания рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='период')
    distribution_status = models.CharField(max_length=20,
                                           choices=STATUSES,
                                           default=STATUS_CREATED,
                                           verbose_name='статус')
    message = models.ForeignKey('MessagesForDistribution',
                                on_delete=models.CASCADE,
                                verbose_name='сообшение',
                                **NULLABLE)

    def __str__(self):
        return f'{self.period} {self.distribution_status}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'


class MessagesForDistribution(models.Model):
    message_theme = models.CharField(max_length=100, verbose_name='тема письма')
    message_body = models.TextField(verbose_name='текст письма')

    def __str__(self):
        return self.message_theme

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    last_attempt = models.DateTimeField(verbose_name='время последней попытки')
    attempt_status = models.BooleanField(default=False, verbose_name='статус попытки')
    mail_response = models.BooleanField(default=False, verbose_name='ответ почтового сервиса')

    def __str__(self):
        return f'{self.attempt_status}/ {self.mail_response}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'




