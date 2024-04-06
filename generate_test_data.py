from datetime import datetime

from main.models import Performance, Product


p1 = Performance(title='Неуслышанные', show_date=datetime(2024, 4, 30), duration_in_of_the_performance='60 минут', description='William Shakespeare classic', age_limit='16+')
p1.save()
p2 = Performance(title='Пингвины', show_date=datetime(2024, 5, 6), duration_in_of_the_performance='1 час 10 минут', description='William Shakespeare classic', age_limit='6+')
p2.save()
p3 = Performance(title='Бешенный хворост', show_date=datetime(2024, 5, 11), duration_in_of_the_performance='1 час 20 минут', description='William Shakespeare classic', age_limit='18+')
p3.save()


p1.is_active = True
p1.save()
p2.is_active = True
p2.save()
p3.is_active = True
p3.save()


prod1 = Product(
    image=None,
    performance=p1,
    show_date=datetime(2024, 4, 30),
    price=800,
    count=50,
    original_price=None,
    is_active=True,
)
prod1.save()
prod2 = Product(
    image=None,
    performance=p2,
    show_date=datetime(2024, 5, 6),
    price=800,
    count=50,
    original_price=None,
    is_active=True,
)
prod2.save()
prod3 = Product(
    image=None,
    performance=p3,
    show_date=datetime(2024, 5, 11),
    price=800,
    count=50,
    original_price=None,
    is_active=True,
)
prod3.save()
prod4 = Product(
    image=None,
    performance=p1,
    show_date=datetime(2022, 6, 1),
    price=800,
    count=50,
    original_price=None,
    is_active=False,
)
prod4.save()
prod5 = Product(
    image=None,
    performance=p1,
    show_date=datetime(2022, 4, 1),
    price=800,
    count=50,
    original_price=None,
    is_active=False,
)
prod5.save()
prod5.save()

prod6 = Product(
    image=None,
    performance=p2,
    show_date=datetime(2022, 7, 8),
    price=800,
    count=50,
    original_price=None,
    is_active=False,
)
prod6.save()
prod6.save()
