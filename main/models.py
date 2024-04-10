from django.db import models
from django.contrib.auth.models import User
import datetime

class Performance(models.Model):
    title = models.CharField(
        max_length=255, blank=False, verbose_name='Название спектакля'
    )
    image = models.ImageField(
        upload_to='images/', verbose_name='Изображение', null=True, blank=True
    )
    is_premiere = models.BooleanField(default=False, verbose_name='Премьера')
    # продолжительность спектакля
    duration_in_of_the_performance = models.TextField(
        verbose_name='Длительность', default='', blank=True
    )
    description = models.TextField(
        verbose_name='Описание', default='', blank=True
    )
    # возрастные ограничения, например 18+, 12+
    age_limit = models.CharField(max_length=5, verbose_name='Возрастное ограничения')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    update_date = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'
    
    def __str__(self):
        return self.title  

class Product(models.Model): 
    performance = models.ForeignKey(
        Performance, on_delete=models.CASCADE, verbose_name='Билет спектакля'
    )
    # дата показа представления
    show_date = models.DateTimeField(
        verbose_name='Дата и время показа', default=datetime.datetime.today
    )
    # цена за один билет
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Цена за билет'
    )
    # цена без скидки (зачеркнутая цена)
    original_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, verbose_name='Цена без скидки(зачеркнуто)'
    )
    # количество билетов макс в зале
    count = models.IntegerField(default=0, verbose_name='Количество билетов')
    # возрастные ограничения, например 18+, 12+

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    update_date = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )

    @property
    def title(self):
        return self.performance.title
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
    
    def __str__(self):
        return self.performance.title   
    
class OrderProduct(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Билет'
    )
    quantity = models.IntegerField(
        verbose_name='Количество'
    )
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name='Цена'
    )

    def __str__(self):
        return f'{self.quantity} of {self.product.performance.title}'


class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = 'CREATED', 'Создан'
        PAYED = 'PAYED', 'Оплачен'
        IN_PROGRESS = 'IN_PROGRESS', 'В обработке'
        CANCELED = 'CANCELED', 'Отменен'
        
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    products = models.ManyToManyField(
        Product, verbose_name='Билеты',
        through=OrderProduct,
        through_fields=('order', 'product')
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=15, choices=Status.choices, default=Status.CREATED
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )
    
    @property
    def is_cancelable(self):
        for product in self.products.all():
            if product.date >= datetime.datetime.today():
                return False
        return True
    
    @property
    def total_price(self):
        return sum([
            order_product.price * order_product.quantity
            for order_product in OrderProduct.objects.filter(order=self)
        ])
        
    class Meta:
        verbose_name = 'Заказ' 
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order from {str(self.user)}'
    