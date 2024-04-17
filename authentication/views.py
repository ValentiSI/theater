from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from main.views import calculate_total_price
from main.models import Order, OrderProduct
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def base_for_profile(request: HttpRequest):
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'base_for_profile.html', {
        'items': items,
        'total_price': total_price
    }))


def register(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return HttpResponse(render(request, 'profile.html', {}))
        else:
            return HttpResponse(render(
                request, 'registration/register.html', {'form': form}
            ))


def logout(request: HttpRequest):
    request.session.flush()
    return redirect('login')


def profile(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return HttpResponse(render(request, 'profile.html', {}))


@login_required
def profile_info(request: HttpRequest):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = request.user
            user.name = form.cleaned_data['name']
            user.surname = form.cleaned_data['surname']
            user.email = form.cleaned_data['email']
            user.phone = form.cleaned_data['phone']
            user.save()
            return redirect('profile_info')
    else:
        form = UserProfileForm()
    return HttpResponse(render(request, 'profile_info.html', {
        'form': form}))


def profile_orders(request: HttpRequest):
    orders = Order.objects.filter(user=request.user)
    orders = sorted(orders, key=lambda order: order.created_at, reverse=True)
    return HttpResponse(render(request, 'profile_orders.html', {
        "orders": orders
    }))


def profile_order_details(request: HttpRequest, order_id: int):
    order = Order.objects.get(id=order_id)
    order_items = OrderProduct.objects.filter(order=order)
    return HttpResponse(render(request, 'profile_order_details.html', {
        "order": order,
        "order_items": order_items
    }))
    