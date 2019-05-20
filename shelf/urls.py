from django.urls import path

from . import views

app_name = 'shelf'

urlpatterns = [
    path('sale/<uuid:group_sale_id>/', views.list_sales, name='list_sales'),
    path('sale/add/', views.add_sale, name='add_sale'),
    path('sale/<uuid:group_sale_id>/receipt/', views.group_sale_receipt, name='group_sale_receipt'),
    path('group-sale/', views.list_group_sales, name='list_group_sales'),
    path('stock/add/', views.add_to_stock, name='add_to_stock'),
    path('branch/', views.list_branches, name='list_branches'),
    path('branch/add/', views.add_branch, name='add_branch'),
    path('product/', views.list_products, name='list_products'),
    path('product/add/', views.add_product, name='add_product'),
]