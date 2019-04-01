import json
import time

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import timezone


@shared_task
def send_email(mail_subject, content, to_emails, attaches=None):
    """
    Gửi email
    :param mail_subject:Tiêu đề của mail
    :param content: Nội dung
    :param to_emails: email người nhận
    :param attaches: file đính kèm
    :return:
    """
    mail = EmailMessage(mail_subject, content, to=[to_emails])
    if attaches:
        for key, value in attaches.items():
            mail.attach(key, value)
    mail.send()
    return "Done"
