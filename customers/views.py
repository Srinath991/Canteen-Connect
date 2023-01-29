from django.shortcuts import render,redirect
# Create your views here.
from.models import Customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
from random import randint
import smtplib
otp=''
api_view(['POST'])
def login_details(request):
    try:
        email=request.POST['email']
        try:
           password=request.POST['key']
           try:
                data=Customer.objects.get(email=email)
                json_data=CustomerSerializer(data).data
                if(json_data['password']==password):
                    return render(request,'index.html')
                else:
                    return redirect('login')
           except:
                return redirect('login')
        except:
            return redirect('login')
    except:
        return redirect('login')
