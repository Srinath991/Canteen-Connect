from django.urls import path
from .views import *
from .views import login_details,register,otp_validation
urlpatterns=[
    path('user/login/',login_details,name='login_details'),
    path("register/",register,name='register'),
    path('user/valid-user/confirm',otp_validation,name='otp_validation')
]