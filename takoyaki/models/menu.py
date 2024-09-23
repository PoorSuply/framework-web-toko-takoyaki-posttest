from django.db import models
from django.core.validators import MinValueValidator

class TakoyakiMenu(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1.000)]
    )
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name
