from django.contrib import admin
from .models import User, TakoyakiMenu, Order, OrderHistory
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)

@admin.register(TakoyakiMenu)
class TakoyakiMenuAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price', 'is_available')
    search_fields = ('item_name',)
    list_filter = ('is_available',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'takoyaki', 'quantity', 'order_date', 'total_price')
    search_fields = ('customer__username', 'takoyaki__item_name')
    list_filter = ('order_date',)

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'action', 'timestamp')
    search_fields = ('order__customer__username', 'action')
    list_filter = ('timestamp',)
