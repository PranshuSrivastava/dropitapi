from django.contrib import admin
from .models import *


class AuctionAdmin(admin.ModelAdmin):
    list_display = ['title', 'current_bid_display', 'bid_count', 'expiry_date', 'active']

    def current_bid_display(self, obj):
        return "£{0}".format(obj.current_bid)


class BidAdmin(admin.ModelAdmin):
    list_display = ['auction', 'value', 'owner', 'created_at']
    list_filter = (
        ('auction',)
    )


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid, BidAdmin)


