from django.contrib import admin
from django.utils.html import format_html_join, format_html
from django.urls import reverse

from .models import Order, OrderProduct, Product, Performance, Category

admin.site.register(Product)
# admin.site.register(Performance)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_vertical = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('_id','user', 'status', 'total_price',
                    'created_at', 'updated_at')
    
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'user__phone'
    )
    
    fields = ('user', 'status', '_id', 'total_price', 'display_order_products')

    readonly_fields = ('display_order_products', '_id', 'total_price')

    list_filter = ('status', 'created_at', 'updated_at')

    actions = ['cancel_order', 'set_payed', 'set_in_progress']
    
    @admin.display(description='Товары в заказе:')
    def display_order_products(self, obj):
        products_data = [
            (
                reverse(
                    'admin:main_product_change',
                    args=[str(order_product.product.id)]
                ),
                f'{order_product.product.title} ({order_product.quantity}) * ' +
                f'{order_product.price} = ' +
                f'{order_product.price * order_product.quantity}'
            )
            for order_product in OrderProduct.objects.filter(order=obj)
        ]

        list_elements = format_html_join(
            '',
            '<li><a href="{}">{}</a></li>',
            products_data
        )

        list_styles = '''
            list-style-type:none; 
            padding: 0; 
            margin: 0;
            font-weight: bold;
        '''

        return format_html(
            '<ul style="{}">{}</ul>',
            list_styles, list_elements
        )
    
    def cancel_order(self, request, queryset):
        queryset.update(status=Order.CANCELED)
    cancel_order.short_description = 'Отменить выбранные заказы'

    def set_payed(self, request, queryset):
        queryset.update(status=Order.PAYED)
    set_payed.short_description = 'Сделать заказы оплаченными'


    def set_in_progress(self, request, queryset):
        queryset.update(status=Order.IN_PROGRESS)
    set_in_progress.short_description = 'Сделать заказы в обработке'

    @admin.display(description='№')
    def _id(self, obj):
        return '\n'.join(
            str(order.id) for order
            in OrderProduct.objects.filter(order=obj)
        )
    
    @admin.display(description='Сумма')
    def total_price(self, obj):
        return obj.total_price

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'user_email', 'user_phone',
                    'user_name', 'user_surname', 'show_date',  
                    'quantity', 'price', 'total_price')

    def user_email(self, obj):
        return obj.order.user.email
    user_email.short_description = 'Email пользователя'
    
    def user_phone(self, obj):
        return obj.order.user.phone
    user_phone.short_description = 'Телефон пользователя'
    
    def user_name(self, obj):
        return obj.order.user.name
    user_name.short_description = 'Имя пользователя'
    
    def user_surname(self, obj):
        return obj.order.user.surname
    user_surname.short_description = 'Фамилия пользователя'
    
    def show_date(self, obj):
        return obj.product.show_date
    show_date.short_description = 'Дата'
    
    @admin.display(description='Сумма')
    def total_price(self, obj):
        return obj.total_price
    