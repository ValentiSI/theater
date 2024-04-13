from audioop import reverse
from django.http import (
    Http404, HttpRequest, HttpResponse, HttpResponseBadRequest
)
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.urls import reverse
from main.utils import q_search

from .models import Order, OrderProduct, Performance, Product, Categories
from .forms import SearchForm

def get_basket_quantity(request: HttpRequest):
    items = request.session.get('basket', [])

    quantities = sum([item['quantity'] for item in items])

    return quantities

def products_view(request: HttpRequest, category_slug=None):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    
    title_text = Categories.objects.get(slug=category_slug).name
    
    if category_slug == None:
        products = Product.objects.filter(is_active=True)
        products = products.order_by('-count', '-show_date')

        if query:
            products = q_search(query)
        
    elif query:
        products = q_search(query)
    else:
        products = Product.objects.filter(category__slug=category_slug, is_active=True)
        products = products.order_by('-count')
        
    if on_sale:
        products = products.filter(original_price__isnull=False)
        
    if order_by and order_by != 'default':
        products = products.order_by(order_by)
            
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        products = products.filter(
            performance__title__icontains=search_form.cleaned_data['query']
        )
        
    paginator = Paginator(products, 1)

    page_number = request.GET.get("page", 1)
    paged_products = paginator.get_page(page_number)
    

    if not request.GET._mutable:
        request.GET._mutable = True

    request.GET['query'] = search_form.cleaned_data['query']

    current_page = paginator.page(page)
    context = {
        'products': current_page,
        'quantities': get_basket_quantity(request),
        'title_text': title_text,
        'slug_url': category_slug
    }
    
    return HttpResponse( render(request, 'main.html', context))

    # return HttpResponse(render(request, 'products.html', {
    #     'products_page': paged_products,
    #     'search_form': search_form
    # }))

def performance_view(request: HttpRequest):
    performance = Performance.objects.all
    
    return HttpResponse(render(request, 'performance.html', {
        'performance': performance
    }))
    
def get_product_for_view(id: int):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Билет не найден')

    if not product.is_active:
        raise Http404('Билет не доступен')

    return product


# def product_view(request: HttpRequest, id: int):
#     return HttpResponse(render(request, 'product.html', {
#         'product': get_product_for_view(id=id)
#     }))

def product_view(request: HttpRequest, id=False, product_slug=False):

    if id:
        product = get_product_for_view(id=id)
    else:
        product = Product.objects.get(slug=product_slug)

    if not product.is_active:
        raise Http404('Билет не доступен')
    return HttpResponse(render(request, 'product.html', {
        'product': product,
        'quantities': get_basket_quantity(request),
    }))


def basket_add_view(request: HttpRequest, id: int):
    product = get_product_for_view(id=id)

    if product.count < 1:
        return redirect('product', id=id)

    basket: list = request.session.get('basket', [])

    found_item = next(
        (item for item in basket if item['product_id'] == id),
        None,
    )

    if found_item is not None:
        found_item['quantity'] = found_item['quantity'] + 1
    else:
        basket.append({
            'product_id': id,
            'quantity': 1
        })

    request.session['basket'] = basket

    return redirect('basket')


def basket_increase_view(request: HttpRequest, id: int):
    items = request.session.get('basket', [])
    product = get_product_for_view(id=id)

    found_item = next(
        (item for item in items if item['product_id'] == id),
        None,
    )

    if found_item is None:
        raise Http404('Товар не найден')

    if product.count < found_item['quantity'] + 1:
        raise HttpRequest('Товар закончился', status=400)

    found_item['quantity'] = found_item['quantity'] + 1

    request.session['basket'] = items

    return HttpResponse(status=200)


def basket_view(request: HttpRequest):
    items = request.session.get('basket', [])

    for item in items:
        item['product'] = Product.objects.get(id=item['product_id'])

    total_price = sum(item['product'].price * item['quantity']
                      for item in items)

    return HttpResponse(render(request, 'basket.html', {
        'items': items,
        'total_price': total_price,
    }))


def basket_clear_view(request: HttpRequest):
    request.session.update({'basket': []})

    return redirect('basket')


def basket_decrease_view(request: HttpRequest, id: int):
    items = request.session.get('basket', [])

    found_item = next(
        (item for item in items if item['product_id'] == id),
        None,
    )

    if found_item is None:
        raise Http404('Товар не найден')

    if found_item['quantity'] > 1:
        found_item['quantity'] = found_item['quantity'] - 1
    else:
        items.remove(found_item)

    request.session['basket'] = items

    return HttpResponse(status=200)


@require_http_methods(["POST"])
def order_view(request: HttpRequest):
    if not request.user.is_authenticated:
        login_page = redirect('login')
        login_page['Location'] += '?next=' + reverse('basket')

        return login_page

    if request.method == 'POST':
        order = Order()
        order.user = request.user
        order.save()

        basket = request.session.get('basket', [])

        if len(basket) == 0:
            return redirect('basket')

        for item in basket:
            product = Product.objects.get(id=item['product_id'])
            if item['quantity'] > product.count:
                return HttpResponseBadRequest('Товара не хватает')

        for item in basket:
            order_product = OrderProduct(order=order)
            order_product.product = Product.objects.get(id=item['product_id'])
            order_product.quantity = item['quantity']
            order_product.product.count -= order_product.quantity
            order_product.price = order_product.product.price
            order_product.product.save()
            order_product.save()

        request.session.update({'basket': []})

        return redirect('get_order', id=order.id)


@require_http_methods(["GET"])
def get_order_view(request: HttpRequest, id: int):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        raise Http404('Заказ не найден')

    return HttpResponse(render(request, 'order.html', {
        'order': order,
        'products': OrderProduct.objects.filter(order=order),
        'quantities': get_basket_quantity(request),
    }))


@require_http_methods(["GET"])
def cancel_order_view(request: HttpRequest, id: int):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        raise Http404('Заказ не найден')

    if order.user != request.user:
        return HttpResponseBadRequest(
            'Вы не можете отменить этот заказ',
            status='403'
        )

    if not order.is_cancelable:
        return HttpResponseBadRequest(
            'Этот заказ уже нельзя отменить. Обратитесь к администратору.',
            status='400'
        )

    for order_product in OrderProduct.objects.filter(order=order):
        order_product.product.count += order_product.quantity
        order_product.product.save()

    order.status = Order.Status.CANCELED
    order.save()

    return redirect('profile')

def calculate_total_price(request):
    shopping_cart = request.session.get('shopping_cart', [])

    total_price = 0
    for item in shopping_cart:
        product_id = item['product_id']
        quantity = item['quantity']
        product = get_product_for_view(product_id=product_id)
        total_price += product.price * quantity

    return total_price
