from django.shortcuts import render
from .models import Order
# Create your views here.
def first_page(requests):
    object_list = Order.objects.all()
    return render(requests,'./index.html',{'object_list':object_list})
