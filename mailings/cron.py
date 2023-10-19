from django.core.mail import send_mail

from djangoProject import settings
from mailings.models import Message, Mailings, Client
from datetime import datetime


def my_scheduled_job():
    for mailing in Mailings.objects.all():
        print(mailing.time_to_send)
        print(datetime.now().time().strftime("%H:%M"))
        if mailing.time_to_send.strftime("%H:%M") < datetime.now().time().strftime("%H:%M"):
            # pk_list_send = mailing.clients.all()
            # clients = [client.email for client in Client.objects.all() if client.pk in pk_list_send]
            send_mail(
                subject='Регистрация',
                message=f'Авторизация удалась.  {[el.email for el in mailing.clients.all()]}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["mister.sid@mail.ru"],
            )

