import logging
from datetime import datetime, timedelta
from smtplib import SMTPException

from dateutil.relativedelta import relativedelta
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from mail.models import MailDistributionSettings, Logs
from mail.services.send_mail import mail_seller

logger = logging.getLogger(__name__)


def my_job():
    maillings = MailDistributionSettings.objects.all()
    print("Скрипт в действии")
    for mailling in maillings:
        status = mailling.distribution_status
        time = datetime.strptime(str(mailling.date_start)[:4], '%H:%M')
        period = mailling.period
        message = mailling.message.__dict__
        clients = [i for i in mailling.clients.all()]
        print('Пошла проверка')
        time_now = datetime.strptime(datetime.now().strftime('%H:%M'), '%H:%M')
        if str(time_now) == str(time):
            try:
                last_attempt = Logs.objects.filter(setting_id=mailling.id).last().last_attempt
                week = last_attempt + timedelta(days=7)
                month = last_attempt + relativedelta(months=1)
                day = last_attempt + timedelta(days=1)
                if status == 'active' and day == datetime.now(
                ) and period == 'daily' or status == 'active' and period == 'weekly' and week == datetime.now(
                ) or status == 'active' and period == 'monthly' and month == datetime.now():
                    for client in clients:
                        print('Рассылка')
                        try:
                            print('Рассылка идет')
                            mail_seller(client, message)
                            Logs.objects.create(attempt_status='Ок', client_id=client.id, setting_id=mailling.id)
                        except SMTPException:
                            print('Рассылка идет с ошибками')
                            Logs.objects.create(attempt_status='Failed', client_id=client.id, setting_id=mailling.id)
            except AttributeError:
                print('Нет лоогов')
                for client in clients:
                        try:
                            print('Рассылка идет')
                            mail_seller(client, message)
                            Logs.objects.create(attempt_status='Ок', client_id=client.id, setting_id=mailling.id)
                        except SMTPException:
                            print('Рассылка идет с ошибками')
                            Logs.objects.create(attempt_status='Failed', client_id=client.id, setting_id=mailling.id)



# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 1 minute
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")