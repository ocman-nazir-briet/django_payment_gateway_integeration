from django.db import models

# Create your models here. 


class Stripe(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=16)
    description = models.TextField()
    source = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source}, -- USD {self.amount}"