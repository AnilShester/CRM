from django.db import models
CATEGORY = (
    ('indoor', 'indoor'),
    ('outdoor', 'outdoor'),
)

class StatusChoice(models.TextChoices):
    PENDING = 'pending'
    OUT_FOR_DELIVERY = 'out for delivery'
    DELIVERED = 'Delivered'
