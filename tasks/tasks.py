from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_status_change_notification(task_title, new_status, user_email):
    subject = f"Task '{task_title}' status changed"
    message = f"The status of task '{task_title}' has been changed to {new_status}."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)


@shared_task
def send_daily_report():
    # Логика отправки отчета о статусе проектов
    pass
