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


    path("products/tags/<tag_slug>/",tag_list,name='tag-list'),

    path('ajax-add-review/<pid>/',ajax_add_review,name='add-review'),

    path('filter-products/',filter_product,name='filter-products'),

    path('add-to-cart/',add_to_cart,name='add-to-cart'),

    path('cart/',cart_items,name='cart-items'),

    path('delete-product/',delete_items,name='delete-product')


]