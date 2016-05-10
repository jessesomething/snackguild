from django.db import models
from django import forms
from django.utils import timezone
from django_countries import fields

class Market(models.Model):
    TRADE_CHOICES = (
    ('Trade', 'Trade'),
    ('Giving', 'Giving'),
    ('Holding', 'Holding')
    )

    STATE_CHOICES = (
    (None, 'Select State'),
    ('NA', ''),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),)

    post_date = models.DateTimeField(
        default=timezone.now)
    trade_type = models.CharField(max_length=100, choices=TRADE_CHOICES, default="Trade")
    snack = models.CharField(max_length=200)
    snack_type = models.CharField(max_length=200)
    country = fields.CountryField(default='US')
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default="NA")
    trader = models.ForeignKey('auth.User')
    trading = models.BooleanField(default=False)
    # thumbnail = models.ImageField(upload_to='market', null=True, blank=True, default="")


    def post(self):
        self.post_date = timezone.now()
        self.save()

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
