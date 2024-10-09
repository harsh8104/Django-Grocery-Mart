
from core.models import *
from django.db.models import Min,Max
def default(request):
    categories=Category.objects.all()
    try:
        address=Address.objects.get(user=request.user)
    except:
        address=None
    vendors=Vendor.objects.all()

    min_max_price=Products.objects.aggregate(Min("price"),Max("price"))


    return {
        'categories':categories,
        'address':address,
        'vendors':vendors,
        'min_max_price':min_max_price
    }
    