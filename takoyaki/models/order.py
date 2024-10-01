from django.db import models
from django.core.validators import MinValueValidator
from .menu import TakoyakiMenu
from django.conf import settings
from django.apps import apps

class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 1}
    )
    takoyaki = models.ForeignKey(TakoyakiMenu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(1.00)])

    def __str__(self):
        return f'Order by {self.customer.username} for {self.quantity} x {self.takoyaki.item_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        OrderHistory = apps.get_model('takoyaki', 'OrderHistory')

        OrderHistory.objects.create(
            order=self,
            action=f"Order {self.id} created/updated for {self.quantity} x {self.takoyaki.item_name}"
        )
