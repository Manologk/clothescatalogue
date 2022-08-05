from django.shortcuts import render
from .models import Products

# Create your views here.
def homepage(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalogue/home.html', context)
