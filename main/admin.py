from django.contrib import admin

from .models import Order, OrderProduct, Product

admin.site.register(Product)

# @admin.register(OrderProduct)
# class OrderProductAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'quantity', 'price',
#                     'order__user', 'order__email', 'created_at', 'updated_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('_id','user', 'status', 'total_price',
                    'created_at', 'updated_at')
    
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'status'
    )
    
    fields = ('user', 'status')
    
    list_filter = ('status', 'created_at', 'updated_at')
    
    actions = ['cancel_order', 'set_payed', 'set_in_progress']
    
    
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
