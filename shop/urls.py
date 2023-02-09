from django.urls import path
from shop import views
app_name = 'shop'
urlpatterns = [
    path('product/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/', views.order, name='order'),
]
