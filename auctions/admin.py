from django.contrib import admin

from .models import User, Category, AuctionList, Bid, Comment, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Watchlist)

@admin.register(AuctionList)
class AuctionListAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "category", "owner", "created_at")


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ("item", "price", "user")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "user", "item")
