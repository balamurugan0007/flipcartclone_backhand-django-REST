from rest_framework import serializers
from app.models import catogory,product,cart,order,address

class catogryserializer(serializers.ModelSerializer):
    class Meta:
        model=catogory
        
        fields='__all__'

class productserializer(serializers.ModelSerializer):
    class Meta :
        model=product
        fields='__all__'

class cartserializer(serializers.ModelSerializer):
    class Meta :
        model=cart
        fields='__all__'


class orderserrilizer(serializers.ModelSerializer):
    class Meta :
        model=order
        fields='__all__'

class addressserializer(serializers.ModelSerializer):
    class Meta :
        model=address
        fields='__all__'



