from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'shop/index-shop.html')


def about(request):
    return render(request, 'blog/index-shop.html')


def search(request):
    return render(request, 'blog/index-shop.html')


def prodview(request):
    return render(request, 'blog/index-shop.html')


def checkout(request):
    return render(request, 'blog/index-shop.html')


def tracker(request):
    return render(request, 'blog/index-shop.html')


def contact(request):
    return render(request, 'blog/index-shop.html')