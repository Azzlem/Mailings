from datetime import datetime

from django.core.mail import send_mail

from djangoProject import settings
from mailings.models import LogMailings


def minute_in_hour(data):
    print(data)
    data = [int(el) for el in data.split(':')]
    if len(data) == 2:
        data = data[0] * 60 + data[1]
        return data
    else:
        return 0


def daytime_comparison(time, date):
    now_time = datetime.now().time().strftime("%H:%M")
    now_date = datetime.now().date().strftime("%Y:%m:%d")
    time = time.strftime("%H:%M")
    date = date.strftime("%Y:%m:%d")
    if date == now_date and minute_in_hour(time) < minute_in_hour(now_time):
        return True
    else:
        return False


def mail_sending(data):
    name, text, emails = data
    result = send_mail(
        subject='Регистрация',
        message=f'Рассылка. \n'
                f'{name}\n'
                f'{text}\n',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
    )

    return result


def log_in(time, name, title, text, success, user_created):
    log_out = LogMailings()
    log_out.time = time
    log_out.mailings_name = name
    log_out.message_title = title
    log_out.message_text = text
    log_out.success = success
    log_out.user_created = user_created
    log_out.save()
