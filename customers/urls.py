from django.urls import path
from .views import *
from .views import login_details
urlpatterns=[
    path('user/login/',login_details)
]