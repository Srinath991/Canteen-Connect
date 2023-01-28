from django.urls import path
from .views import *
from .views import login_details,confirm_otp
urlpatterns=[
    path('user/login/',login_details),
    path("confirm/",confirm_otp,name='confirm'),
]