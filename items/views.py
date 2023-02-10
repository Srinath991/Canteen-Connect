from django.shortcuts import render,redirect
# Create your views here.
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,renderer_classes,authentication_classes,permission_classes
from.serializers import itemsserializer
from .models import item

@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def login_info(request):
    return Response(template_name='login.html')
@api_view(['GET'])
@renderer_classes([JSONRenderer])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_all_products(request):
    scr_data=itemsserializer(item.objects.all(),many=True)
    data={"data":scr_data.data}
    return Response(data)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_product_by_category_id(request,pk=None):
    scr_data=itemsserializer(item.objects.filter(categoryID=pk),many=True)
    data={"data":scr_data.data}
    return Response(data=data)
    