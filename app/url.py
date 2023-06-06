
from django.urls import path
from app import views
from app import post_views

urlpatterns = [
    
    path('catogory/',views.catogorydetail),
    path('products',views.productdetails),
    path('cartdetails',views.cartdetail),
    path('address',views.addressdetail),
    path('orderdetails',views.orderdetail),



#post views path

    path('additems/product',post_views.productspost),
    path('additems/order',post_views.orderpost),
    path('additems/cart',post_views.cartpost),
    path('additems/catogory',post_views.catogorypost),
    path('additems/address',post_views.adresspost)

    
]
