from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
import base64
from django.core.files.base import ContentFile
from urllib.request import urlopen

from .models import UserProfile , Product
import os
from django.conf import settings
@csrf_exempt
@api_view(['GET'])
def GetAllProducts(request):
    products = Product.objects.all()
    
    pro = []
    for i in range(0,len(products)):
        # en = (settings.ENDPOINT + products[i].photos.url).encode("utf-8")
        # en = base64.b64encode(en)
        x = {
            'id': products[i].id,
            'title': products[i].title,
            'description': products[i].description,
            'creation_date': products[i].creation_date,
            'category': products[i].category,
            'price': products[i].price,
            'photos': settings.ENDPOINT + products[i].photos.url,
            # 'photos': str(en),
            'rate': products[i].rate,

            'username': products[i].Owner.username
        }

        
        pro.append(x)
    return JsonResponse({'Products':pro , 'message':'Done'},status = 200)

