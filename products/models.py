from django.db import models
from django.conf import settings


class Product(models.Model):
    CATEGORIES = (
        ('ACS', 'Accessories'),
        ('CON', 'Console'),
        ('GAM', 'Game'),
        ('ECS', 'Electronics'),
        ('COM', 'Computers'),
        ('AUT', 'Automotive'),
        ('ANT', 'Antiques'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=3, choices=CATEGORIES)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    start_price = models.DecimalField(decimal_places=4, max_digits=8)
    buy_now_price = models.DecimalField(decimal_places=4, max_digits=8)

    verbose_name_plural = 'products'

    def __str__(self):
        return "Title: " + self.title

    class Meta:
        db_table = 'product'


class Auction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    bids_number = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "ID: " + str(self.pk) + "Product" + str(self.product)


class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return "User ID: " + str(self.user_id) + " Auction ID: " + str(self.auction_id)


class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()

    def __str__(self):
        return "User ID: " + str(self.user_id) + " Auction ID : " + str(self.auction_id) + " " + str(self.bid_time)

