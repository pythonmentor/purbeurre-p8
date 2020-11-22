from django.urls import path

from .views import FavoriteListView, FavoriteDetailView

app_name = 'favorites'

urlpatterns = [
    path('', FavoriteListView.as_view(), name="list"),
]