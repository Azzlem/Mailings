from django.core.mail import send_mail

from djangoProject import settings
from mailings.models import Message


def my_scheduled_job():
    send_mail(
        subject='Регистрация',
        message=f'Авторизация удалась.  {"token"}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['mister.sid@mail.ru'],
    )
