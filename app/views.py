from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from app.models import product,address,catogory,cart,order


@api_view(['GET'])
def addressdetail(request):
    item=address.objects.all()
    serializer=addressserializer(item,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productdetails(request):
    posts=product.objects.all()
    post_serilizer=productserializer(posts,many=True)
    return Response(post_serilizer.data)


@api_view(['GET'])
def catogorydetail(request):
    save_post=catogory.objects.all()
    savepost_serilizer=catogryserializer(save_post,many=True)
    return Response(savepost_serilizer.data)


@api_view(['GET'])
def cartdetail(request):
    comments=cart.objects.all()
    commet_serilzer=cartserializer(comments,many=True)
    return Response(commet_serilzer.data)

@api_view(['GET'])
def orderdetail(request):
    likes=order.objects.all()
    like_serilizer=orderserrilizer(likes,many=True)
    return Response(like_serilizer.data)



