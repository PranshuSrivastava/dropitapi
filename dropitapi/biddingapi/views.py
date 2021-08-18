from .models import Auction
from datetime import datetime, timedelta


# Create your views here.
def update_active_bidding_orders(request):
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    expired_bid_ids = Auction.objects.all()
    for val in expired_bid_ids:
        if val.expiry_date.time() < current_time and val.expiry_date.date() < current_date:
            val.active =False
            val.save()
            print("done")
        # expired_bid_ids.update()
    print("########################################################################################################################################################")
    return 0