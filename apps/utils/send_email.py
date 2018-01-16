from random import choice

from django.core.mail import send_mail

from users.models import EmailVerifyCode
from wechatRead.settings_dev import EMAIL_FROM


def generate_code():
    seeds = '1234567890qwertyuiopasdfghjklzxcvbnm'
    random_str = []
    for i in range(6):
        random_str.append(choice(seeds))
    return ''.join(random_str)

def send_email(email, send_type='register'):

    email_record = EmailVerifyCode()
    code = generate_code()
    email_record.email = email
    email_record.code = code
    email_record.send_type = 'register'

    if send_type == 'register':
        email_title = '微信读书注册验证码'
        email_body = '微信读书的注册验证码为： {0}'.format(code)
        send_mail(email_title, email_body, EMAIL_FROM, [email])
        email_record.save()

    return code
