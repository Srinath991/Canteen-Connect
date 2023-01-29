from django.core.mail import send_mail
send_mail(
        'Subject here',
        f'Here your otp is {otp}',
        '991techsri@gmail.com',
        ['srinathvsrinathv863@gmail.com'],
        fail_silently=False)