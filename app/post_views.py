from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
#from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def catogorypost(request):
    catogory_serializer=catogryserializer(data=request.data)
    if catogory_serializer.is_valid():
        
        catogory_serializer.save()
        return Response(catogory_serializer.data)
    


@api_view(['POST'])
def productspost(request):
    products_serilizer=productserializer(data=request.data)
    if products_serilizer.is_valid():
        
        products_serilizer.save()
        return Response(products_serilizer.data)
    

@api_view(['POST'])
def cartpost(request):
    cart_serilizer=cartserializer(data=request.data)
    if cart_serilizer.is_valid():
        cart_serilizer.save()
        return Response(cart_serilizer.data)
    
@api_view(['POST'])
def orderpost(request):
    order_serilzer=orderserrilizer(data=request.data)
    if order_serilzer.is_valid():
        order_serilzer.save()
        return Response(order_serilzer.data)
    
@api_view(['POST'])
def adresspost(request):
    address_serlizer=addressserializer(data=request.data)
    if address_serlizer.is_valid():
        address_serlizer.save()
        return Response(address_serlizer.data)
