from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.utils.html import mark_safe



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10 , blank=True)
    address=models.CharField(default='',max_length=250 , blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural="User Profiles"
        verbose_name="User Profile"

    
class Product(models.Model):
    title=models.CharField(max_length=150 , blank=True)
    description = models.CharField(max_length=500 , blank=True)
    creation_date=models.DateTimeField(default=datetime.now)
    category= models.CharField(max_length=20,default='' , blank=True)
    price=models.FloatField(blank=True)
    photos=models.ImageField(null=True , blank=True ,upload_to='photos/products/%Y/%m/%d/')

    rate=models.FloatField( blank=True)
    Rated=models.ManyToManyField(User,related_name="rated",through="Rated_Products")
    
    Owner = models.ForeignKey(User, default=0 ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="Products"
        verbose_name="Product"

    def product_photo_preview(self):
        return mark_safe('<img src="{url}" width="150" height="150" />'.format(url=self.photos.url))


class Rated_Products(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    value=models.FloatField(blank=True, default=0)
    def __str__(self):
        return self.value
    class Meta:
        verbose_name_plural="Rated_Products"
        verbose_name="Rated_Product"