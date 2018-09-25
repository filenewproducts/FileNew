from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
from .models import ProductType


def product_list(request):
    productTypes = ProductType.objects.filter(
        created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'bookClass/product_list.html', {'productTypes': productTypes})
