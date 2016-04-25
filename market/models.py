from django.db import models
from django.utils import timezone

class Market(models.Model):
    trader = models.ForeignKey('auth.User')
    snack = models.CharField(max_length=200)
    trade_type = models.CharField(max_length=200)
    snack_type = models.CharField(max_length=200)
    post_date = models.DateTimeField(
        default=timezone.now)

    def post(self):
        self.post_date = timezone.now()
        self.save()

    def __str__(self):
        return self.snack

# Create your models here.
