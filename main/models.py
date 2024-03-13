from django.db import models

class Ticket(models.Model):
    title = models.CharField(
        max_length=255, blank=False, verbose_name='Название спектакля')
    description = models.TextField(verbose_name='Описание')
    # цена за один билет
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена за билет')
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Цена со скидкой')
    # количество билетов макс в зале
    count = models.IntegerField(default=0, verbose_name='Количество билетов')
    # возрастные ограничения, например 18+, 12+
    age_limit = models.CharField(max_length=3, verbose_name='Возрастное ограничения')
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
    
    def __str__(self):
        return self.title   