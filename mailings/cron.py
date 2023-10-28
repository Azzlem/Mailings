from mailings.models import Mailings
from datetime import datetime, timedelta, date
import calendar

from mailings.utils import mail_sending, log_in, daytime_comparison


def my_scheduled_job():
    for mailing in Mailings.objects.all():
        print(type(mailing.day_start))

        if daytime_comparison(mailing.time_to_send, mailing.day_start):
            data = mailing.name, mailing.message.text, [el.email for el in mailing.clients.all()]
            result = mail_sending(data)
            log_in(
                datetime.now().strftime("%Y:%m:%d" " " "%H:%M"),
                mailing.name,
                mailing.message.name,
                mailing.message.text,
                result,
                mailing.user_creator,
            )
            if not result:
                data = 'Ошибка', f'рассылка {mailing.name}', mailing.user_creator
                mail_sending(data)
                mailing.time_to_send = mailing.time_to_send + timedelta(minutes=20)
            elif mailing.periodicity == 'Раз в день':
                mailing.day_start = mailing.day_start + timedelta(days=1)
            elif mailing.periodicity == 'Раз в неделю':
                mailing.day_start = mailing.day_start + timedelta(days=7)
            elif mailing.periodicity == 'Раз в месяц':
                today = date.today()
                days = calendar.monthrange(today.year, today.month)[1]
                mailing.day_start = mailing.day_start + timedelta(days=days)
            mailing.save()
