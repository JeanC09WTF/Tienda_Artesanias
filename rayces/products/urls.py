from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#vista principal
    path('reservas/', views.reservas, name='reservas'),
    path('acerca/', views.acerca, name='acerca'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('reserva_exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
    path('products/', views.index, name='product_list'),#cambie product_list por index
    path('catalog/', views.product_catalog, name='product_catalog'),
    path('decoracion/', views.decoracion_prod, name='decoracion_prod'),
    path('ropa/', views.ropa_pro, name='ropa_pro'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
 