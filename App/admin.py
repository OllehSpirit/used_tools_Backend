from django.contrib import admin
from .models import UserProfile , Product , User

# Register your models here.

admin.site.unregister(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')
    # readonly_fields = ('id',)
    search_fields = ['username']
    list_filter = ('is_staff', 'is_superuser')
admin.site.register(User, CustomUserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user_id' , 'user' , 'phone' , 'address' )
    search_fields = ['user']
    list_filter = ( 'address' , )
admin.site.register(UserProfile , UserProfileAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' , 'description' , 'creation_date' , 'price' , 'category' , 'photos' , 'Owner')
    search_fields = ['title' , 'description']
    readonly_fields = ['product_photo_preview']
    list_filter = ('Owner',)
admin.site.register(Product , ProductAdmin)

