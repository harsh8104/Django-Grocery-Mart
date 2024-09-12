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

def vendor_list(request):
    vendor=Vendor.objects.all()
    context={
        'vendors':vendor
    }
    return render(request,'core/vendor.html',context)


def vendor_list_detail(request,vid):
    vendor=Vendor.objects.get(vid=vid)
    product=Products.objects.filter(vendor=vendor,product_status="published")
    context={
        'vendor':vendor,
        'products':product
    }
    return render(request,'core/vendor-detail.html',context)


def product_detail(request,pid):
    product=Products.objects.get(pid=pid)

    p_image=product.p_images.all()
    context={
        'product':product,
        'p_image':p_image
    }
    return render(request,'core/product-detail.html',context)

