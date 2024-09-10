from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
# Create your views here.


def index(request):
    # product=Products.objects.all().order_by("-id")
    product=Products.objects.filter(product_status="published",featured=True)
    context={
        'products':product
    }
    return render(request,'core/index.html',context)


def prodcut_list(request):
    product=Products.objects.filter(product_status="published")
    context={
        'products':product
    }
    return render(request,'core/product-list.html',context)


def category_product_list(request,cid):
    category=Category.objects.get(cid=cid)
    product=Products.objects.filter(category=category,product_status="published")
    context={
        'category':category,
        'products':product
    }
    return render(request,'core/category-list.html',context)



def category_list(request):
    category=Category.objects.all()
    context={
        'categories':category
    }
    return render(request,'core/category.html',context)

