from django.shortcuts import render,redirect
# Create your views here.
from.models import Customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email import email_to_user
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
@api_view(['GET'])
def register(request):
    if request.method=="GET":
        return render(request,'register.html')
@api_view(['POST'])
def otp_validation(request):
    thrd=email_to_user('srinathvsrinathv863@gmail.com')
    thrd.start()
    try:
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            try:
                Customer.objects.get({'email':email})
                return redirect('login')
            except:
                email_to_user(email)
                return redirect('otp')

        else:
            return render(request,'register.html')
        
    except:
        return render(request,'register.html')
