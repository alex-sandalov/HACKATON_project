from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import *


def product_list(request, category_slug=None):
    """ Лист продуктов """

    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/product/index.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def home(request):
    return render(request, 'shop/product/home.html')



