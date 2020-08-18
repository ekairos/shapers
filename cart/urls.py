from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_cart, name='get_cart'),
    path('add/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<str:product_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('update/<str:product_id>/', views.update_cart, name='update_cart')
]
