from django.contrib import admin
from core.models import *

# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model=ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImagesAdmin]
    list_display=['user','title','product_image','category','vendor','price','featured','product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image']

class VendorAdmin(admin.ModelAdmin):
    
    list_display=['title','vendor_image']

class CartsOrderAdmin(admin.ModelAdmin):
    list_display=['user','price','paid_track','order_date']


class CartsOrderItemsAdmin(admin.ModelAdmin):
    list_display=['order','invoice_no','item','order_img','quantity','price','total']


class ProductsReviewAdmin(admin.ModelAdmin):
    list_display=['user','product','review','rating']


class WishlistAdmin(admin.ModelAdmin):
    list_display=['user','product','date']

class AddressAdmin(admin.ModelAdmin):
    list_display=['user','address','status']


admin.site.register(Products,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(CartOrder,CartsOrderAdmin)
admin.site.register(CartItems,CartsOrderItemsAdmin)
admin.site.register(Product_Review,ProductsReviewAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)