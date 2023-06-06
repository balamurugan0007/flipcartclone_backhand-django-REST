from django.db import models


# Create your models here.
class user(models.Model):
    name=models.CharField( max_length=150,blank=False,null=False)


class catogory(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='static/products',null=False,blank=False)
    description=models.TextField(max_length=300,null=False,blank=False)
    date=models.DateField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self) :
        return self.name

    


class product(models.Model):
    catogory=models.ForeignKey(catogory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=False,null=False)
    brand=models.CharField(max_length=170)
    old_price=models.IntegerField(blank=False,null=False)
    new_price=models.IntegerField(blank=False,null=False)
    ratings=models.FloatField(blank=False,null=False)
    stocks=models.IntegerField(blank=False,null=False)
    
    image=models.ImageField(upload_to='static/products',null=False,blank=False)
    image1=models.ImageField(upload_to='static/products',null=True,blank=True)
    image2=models.ImageField(upload_to='static/products',null=True,blank=True)
    image3=models.ImageField(upload_to='static/products',null=True,blank=True)
    description=models.TextField(max_length=300,null=False,blank=False)
    date=models.DateField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    seller_name=models.CharField(max_length=100,blank=False,null=False)
    

    def __str__(self) :
        return self.name
    
    

    
class review(models.Model):
    post=models.ForeignKey(product,on_delete=models.CASCADE)
    name=models.ForeignKey(user,on_delete=models.CASCADE)
    comments=models.TextField()
    ratings=models.IntegerField(blank=False,null=False)
    date=models.DateField()
    time=models.TimeField()
    
    
    
class cart(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    name=models.ForeignKey(user,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()



class address(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    phone=models.IntegerField(blank=False,null=False)
    address=models.TextField(blank=False,null=False)
    pincode=models.CharField(max_length=100,blank=False,null=False)
    landmark=models.CharField(max_length=100,blank=False,null=False)



class order(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    name=models.ForeignKey(user,on_delete=models.CASCADE)
    qty=models.IntegerField()
    address=models.ForeignKey(address,on_delete=models.CASCADE)
    time=models.TimeField()
    date=models.DateField()
    
