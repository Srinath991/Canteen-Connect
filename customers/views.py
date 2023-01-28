from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from.models import Customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
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
                    return redirect('confirm')
                else:
                    return redirect('login')
           except:
                return redirect('login')
        except:
            return redirect('login')
    except:
        return redirect('login')
def confirm_otp(request):
    return render(request,'otp.html')