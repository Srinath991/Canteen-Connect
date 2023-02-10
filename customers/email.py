from django.core.mail import send_mail
from random import randint
from threading import Thread
otp=''
class email_to_user(Thread):
    def __init__(self,email) -> None:
        super().__init__()
        self.email=email
    def send(self):
        global otp
        for i in range(5):
            otp+=str(randint(0,9))
        send_mail(
        subject='991 TECH SRI',
        message=f"Registration verification code {otp}\n ",
        from_email='991techsri@gmail.com',
        recipient_list=(self.email,),
        fail_silently=False,)
        otp=''
        print('email send successfully')
    def run(self):
        self.send()
