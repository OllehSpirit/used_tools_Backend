from django.urls import path
from . import views


urlpatterns=[
    path( 'products' , views.GetAllProducts , name='GetAllProducts' ), 
    
]