from django.shortcuts import render
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            order_created(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm

    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})