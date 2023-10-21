from django.core.mail import send_mail

from djangoProject import settings
from mailings.models import Message, Mailings, Client
from datetime import datetime

from mailings.utils import minute_in_hour


def my_scheduled_job():
    for mailing in Mailings.objects.all():
        print(mailing.time_to_send)
        print(datetime.now().time().strftime("%H:%M"))
        if minute_in_hour(mailing.time_to_send.strftime("%H:%M")) <= minute_in_hour(datetime.now().time().strftime("%H:%M")):
            # pk_list_send = mailing.clients.all()
            # clients = [client.email for client in Client.objects.all() if client.pk in pk_list_send]
            send_mail(
                subject='Регистрация',
                message=f'Рассылка. \n'
                        f'{mailing.message.name}\n'
                        f'{mailing.message.text}\n',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[el.email for el in mailing.clients.all()],
            )
        # else:
        #     send_mail(
        #         subject='Регистрация',
        #         message=f'Авторизация удалась. {mailing.time_to_send} {datetime.now().time().strftime("%H:%M")}'
        #                 f'Хуйня переделывай',
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=['mister.sid@mail.ru',],
        #     )

