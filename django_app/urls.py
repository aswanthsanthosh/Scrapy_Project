from django.urls import path
from .views import scrape_view, home_view, products_view, clear_db

urlpatterns = [
    path('scrape/', scrape_view, name='scrape'),
    path('', home_view, name='home'),
    path('products/', products_view, name='products'),
    path('clear_db/', clear_db, name='clear_db')
]