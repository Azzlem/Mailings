from django.core.mail import send_mail

from djangoProject import settings
from mailings.models import Mailings


def minute_in_hour(data):
    data = [int(el) for el in data.split(':')]
    data = data[0] * 60 + data[1]

    return data


def mail_sending(data):
    name, text, status, emails = data
    send_mail(
        subject='Регистрация',
        message=f'Рассылка. \n'
                f'{name}\n'
                f'{text}\n'
                f'{status}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
    )
