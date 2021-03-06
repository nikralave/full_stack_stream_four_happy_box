from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Image
from reviews.forms import ReviewForm
from reviews.models import Review


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    wishlist = request.session.get('wishlist', {})
    in_wishlist = id in wishlist
    return render(request, 'products/product_list.html', {'products':products,'categories':categories, 'in_wishlist': in_wishlist})
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = Image.objects.filter(product__name=product)
    form = ReviewForm()
    wishlist = request.session.get('wishlist', {})
    in_wishlist = id in wishlist
    return render(request, 'products/product_detail.html', {'product':product, 'images':images, 'review_form': form, 'in_wishlist': in_wishlist})
    
def get_cat_products(request, category):
    products = Product.objects.filter(category__name=category)
    return render(request, 'products/product_list.html', {'products':products, 'category_filtered':category})

