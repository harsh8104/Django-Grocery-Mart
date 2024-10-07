
from core.models import *
def default(request):
    categories=Category.objects.all()
    try:
        address=Address.objects.get(user=request.user)
    except:
        address=None
    vendors=Vendor.objects.all()
    return {
        'categories':categories,
        'address':address,
        'vendors':vendors
    }
    