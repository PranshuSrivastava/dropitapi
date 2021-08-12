from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
import time
User = settings.AUTH_USER_MODEL

class AuctionManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(active=True)

    def expired(self):
        return super().get_queryset().filter(active=False)


class Auction(models.Model):
    title = models.CharField(max_length=255)
    current_bid = models.FloatField()
    bid_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    live_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    active = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class IsActiveManager(models.Manager):
    def get_queryset(self):
        return super(IsActiveManager, self).get_queryset().filter(active=True).order_by('-created_at')

    # def __str__(self):
    #     return self.title

    # def __unicode__(self):
    #     return self.title

    # objects = models.Manager()
    # AuctionManager = AuctionManager()


class BidManager(models.Manager):
    def current(self, auction):
        return super().get_queryset().filter(auction=auction).order_by('-created_at')


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    value = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{0} - {1}".format(self.auction, self.value)

    objects = models.Manager()
    BidManager = BidManager()

    