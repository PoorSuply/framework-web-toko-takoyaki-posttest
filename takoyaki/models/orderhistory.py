from django.db import models
from django.apps import apps  # Tambahkan import ini

class OrderHistory(models.Model):
    order = models.ForeignKey('takoyaki.Order', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Order {self.order.id} - {self.action}"
