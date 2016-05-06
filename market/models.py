from django.db import models
from django.utils import timezone

class Market(models.Model):
    post_date = models.DateTimeField(
        default=timezone.now)
    trade_type = models.CharField(max_length=200)
    snack = models.CharField(max_length=200)
    snack_type = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default="United States")
    state = models.CharField(max_length=200, default="")
    trader = models.ForeignKey('auth.User')
    trading = models.BooleanField(default=False)

    def post(self):
        self.post_date = timezone.now()
        self.save()

    def get_trader(self):
        return self.trader

    def __str__(self):
        return self.snack

class Trade_Cart(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    snack = models.CharField(max_length=200)
    snack_type = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default="United States")
    state = models.CharField(max_length=200, default="")
    trader = models.ForeignKey('auth.User')

    def post(self):
        self.trade_date = timezone.now()

    def __str__(self):
        return self.snack

# Create your models here.
