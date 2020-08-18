from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_cart, name='get_cart'),
    path('add/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
]
