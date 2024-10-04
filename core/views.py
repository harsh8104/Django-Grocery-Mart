from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from core.models import *
from django.shortcuts import render,get_object_or_404
from taggit.models import Tag
from django.db.models import Count,Avg
from core.forms import ProductReviewForm
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
    products=Products.objects.filter(category=product.category).exclude(pid=pid)

    reviews=Product_Review.objects.filter(product=product).order_by("-date")

    avg_rating=Product_Review.objects.filter(product=product).aggregate(rating=Avg('rating'))

    review_form=ProductReviewForm()

    p_image=product.p_images.all()
    context={
        'product':product,
        'p_image':p_image,
        'reviews':reviews,
        'products':products,
        'avg_rating':avg_rating,
        'review_form':review_form
    }
    return render(request,'core/product-detail.html',context)

def tag_list(request,tag_slug=None):
    product=Products.objects.filter(product_status="published").order_by("-id")
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        products=product.filter(tags=tag)
    context={
        "products":products,
        "tag":tag,
    }
    return render(request,'core/tag.html',context)


def ajax_add_review(request,pid):
    product=Products.objects.get(pid=pid)
    user=request.user

    review=Product_Review.objects.create(
        user=user,
        product=product,
        review=request.POST.get('review'),
        rating=request.POST.get('rating')
    )

    context={
        'user':user.username,
        'review':request.POST.get('review'),
        'rating':request.POST.get('rating'),
        'date':review.date
    }

    avg_reviews=Product_Review.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {'bool':True,
        'context':context,
        'avg_rating':avg_reviews}
    )
    
