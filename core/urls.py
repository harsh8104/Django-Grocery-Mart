from django.urls import path
from core.views import *

app_name='core'

urlpatterns = [
    path('',index,name='index'),


    path('category/',category_list,name='category'),
    path('category/<cid>/',category_product_list,name="category-product-list"),

    path('vendors/',vendor_list,name="vendor-list"),
    path('vendor/<vid>/',vendor_list_detail,name="vendor-detail"),
    
    path('products/',prodcut_list,name='products'),
    path('product/<pid>/',product_detail,name="product-detail"),

]