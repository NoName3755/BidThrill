from .models import Watchlist, Bid

def is_in_watchlist(user, item):
    inwatchlist = False
    if Watchlist.objects.filter(user=user, item=item).exists():
        inwatchlist = True
    return inwatchlist
    
