from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauth.models import User
# Create your models here.

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Tags(models.Model):
    pass

STATUS_CHOICE=(
    ("process","Processing"),
    ("shipped","Shipped"),
    ("deliverd","Delivered"),
)

STATUS=(
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("rejected","Rejected"),
    ("in_review","In Review"),
    ("published","Published"),
)

STATUS_CHOICE=(
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★"),
)

class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=30,prefix='cat',alphabet='abcdefgh12345')
    title=models.CharField(max_length=100,default='Food')
    image=models.ImageField(upload_to=user_directory_path,default="category.jpg")
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title


class Vendor(models.Model):
    vid=ShortUUIDField(unique=True,length=10,max_length=30,prefix='ven',alphabet='abcdefgh12345')
    title=models.CharField(max_length=100,default='Nestify Vendor')
    image=models.ImageField(upload_to=user_directory_path,default="vendor.jpg")
    description=models.TextField(null=True,blank=True,default='I am an amazing vendor')
    address=models.CharField(max_length=100,default='S.G Highway Ahmedabad')
    contact=models.CharField(max_length=100,default='+91 123456789')
    chat_resp_time=models.CharField(max_length=100,default='100')
    shipping_on_time=models.CharField(max_length=100,default='100')
    authentic_rating=models.CharField(max_length=100,default='100')
    days_return=models.CharField(max_length=100,default='100')
    warranty_period=models.CharField(max_length=100,default="100")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Vendors"
    
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title



class Products(models.Model):
    pid=ShortUUIDField(unique=True,length=10,max_length=30,prefix='pro',alphabet='abcdefgh12345')
    title=models.CharField(max_length=100,default='Fresh Pear')
    image=models.ImageField(upload_to=user_directory_path,default="product.jpg")
    description=models.TextField(null=True,blank=True,default='This is the product')

    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='category')

    price=models.DecimalField(max_digits=9999999,decimal_places=2,default="1.99")
    old_price=models.DecimalField(max_digits=9999999,decimal_places=2,default="2.99")

    specifications=models.TextField(null=True,blank=True,default="This is special product")
    # tags=models.ForeignKey(Tags,on_delete=models.SET_NULL,null=True)

    product_status=models.CharField(choices=STATUS,max_length=10,default='in_review')
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)
    featured=models.BooleanField(default=False)
    digital=models.BooleanField(default=False)

    sku=ShortUUIDField(unique=True,length=5,max_length=20,prefix="sku",alphabet="1234567890")
    date=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Products"
    
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price=(self.price/self.old_price)*100
        return new_price
    

class ProductImages(models.Model):
    images=models.ImageField(upload_to="product-images",default="product.jpg")
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"


class CartOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=9999999,decimal_places=2,default="1.99")
    paid_track=models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now_add=True)
    product_status=models.CharField(choices=STATUS_CHOICE,max_length=30,default='Processing')

    class Meta:
        verbose_name_plural = "Cart Orders"
    

class CartItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    product_status=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    quantity=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=9999999,decimal_places=2,default="1.99")
    total=models.DecimalField(max_digits=9999999,decimal_places=2,default="1.99")
    invoice_no=models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Cart Items"
    
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))



    
    

class Product_Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    review=models.TextField()
    rating=models.IntegerField(choices=STATUS_CHOICE,default=None)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"
    


    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating



    

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"
    


    def __str__(self):
        return self.product.title

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=100,null=True)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"
    
    def __str__(self):
        return self.address


