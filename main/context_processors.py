from django.http import HttpRequest


def get_basket_quantity(request: HttpRequest):
    items = request.session.get('basket', [])

    quantities = sum([item['quantity'] for item in items])

    return quantities


def basket_context_processor(request):
    return {"basket_quantity": get_basket_quantity(request)}
