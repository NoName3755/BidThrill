from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("item/<int:id>", views.item_view, name="item_view"),
    path("item/<int:id>/add_or_remove_watchlist", views.add_or_remove_watchlist, name="add_or_remove_watchlist"),
    path("item/<int:id>/bid", views.item_bid, name="item_bid"),
    path("item/<int:id>/comment", views.comment, name="comment"),
    path("item/<int:id>/comment_delete", views.comment_delete, name="comment_delete"),
    path("closed_listing", views.closed_listing, name="closed_listing"),
    path("watchlists", views.watchlist_view, name="watchlist"),
    path("categories", views.categories_view, name="categories"),
    path("category/<str:category>", views.category_view, name="category"),
]
