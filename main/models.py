from django.db import models

class Ticket(models.Model):
    title = models.CharField(
        max_length=255, blank=False, verbose_name='Название спектакля'
    )
    image = models.ImageField(
        upload_to='images/', verbose_name='Изображение', null=True, blank=True
    )
    description = models.TextField(
        verbose_name='Описание', default='', blank=True
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
    age_limit = models.CharField(max_length=3, verbose_name='Возрастное ограничения')
    is_activ = models.BooleanField(default=True, verbose_name='Активен')
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    update_date = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )
    
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
    
    def __str__(self):
        return self.title   