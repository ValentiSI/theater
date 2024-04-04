from datetime import datetime

from main.models import Performance, Product


p1 = Performance(title='Hamlet', show_date=datetime(2022, 4, 1), duration_in_of_the_performance='2 hours', description='William Shakespeare classic', age_limit='16+')
p1.save()
p2 = Performance(title='The Merchant of Venice', show_date=datetime(2022, 5, 1), duration_in_of_the_performance='4 hours', description='William Shakespeare classic', age_limit='18+')
p2.save()
p3 = Performance(title='A Midsummer Night\'s Dream', show_date=datetime(2022, 6, 1), duration_in_of_the_performance='3 hours', description='William Shakespeare classic', age_limit='16+')
p3.save()
p4 = Performance(title='Othello', show_date=datetime(2022, 7, 1), duration_in_of_the_performance='3 hours', description='William Shakespeare classic', age_limit='18+')
p4.save()

p1.is_active = True
p1.save()
p2.is_active = False
p2.save()
p3.is_active = True
p3.save()
p4.is_active = True
p4.save()

prod1 = Product(
    image=None,
    performance=p1,
    show_date=datetime(2022, 4, 1),
    price=150,
    count=5,
    original_price=None,
    is_active=True,
)
prod1.save()
prod2 = Product(
    image=None,
    performance=p2,
    show_date=datetime(2022, 5, 1),
    price=200,
    count=10,
    original_price=None,
    is_active=True,
)
prod2.save()
prod3 = Product(
    image=None,
    performance=p3,
    show_date=datetime(2022, 6, 1),
    price=120,
    count=7,
    original_price=None,
    is_active=True,
)
prod3.save()
prod4 = Product(
    image=None,
    performance=p4,
    show_date=datetime(2022, 7, 1),
    price=180,
    count=15,
    original_price=None,
    is_active=True,
)
prod4.save()
prod5 = Product(
    image=None,
    performance=p1,
    show_date=datetime(2022, 4, 1),
    price=200,
    count=10,
    original_price=None,
    is_active=True,
)
prod5.save()
prod5.save()

