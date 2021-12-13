from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add/<uuid:product_id>/', views.add_cart, name='cart_add'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<uuid:product_id>/', views.cart_remove, name='cart_remove'),
    path('clear/<uuid:product_id>/', views.full_remove, name='cart_clear'),
]