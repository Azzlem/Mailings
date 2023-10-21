from django.core.mail import send_mail

from djangoProject import settings
from mailings.models import Message, Mailings, Client
from datetime import datetime

from mailings.utils import minute_in_hour, mail_sending


def my_scheduled_job():
    for mailing in Mailings.objects.all():
        print(mailing.time_to_send)
        print(datetime.now().time().strftime("%H:%M"))
        if minute_in_hour(mailing.time_to_send.strftime("%H:%M")) <= minute_in_hour(
                datetime.now().time().strftime("%H:%M")) and mailing.status == 'Создана':
            # pk_list_send = mailing.clients.all()
            # clients = [client.email for client in Client.objects.all() if client.pk in pk_list_send]
            data = mailing.message.name, mailing.message.text, mailing.status, [el.email for el in
                                                                                mailing.clients.all()]
            mail_sending(data)
            mailing.status = 'Запущена'
            mailing.save()


def reset():
    for mailing in Mailings.objects.all():
        if mailing.status == 'Запущена':
            mailing.status = 'Создана'
            mailing.save()
