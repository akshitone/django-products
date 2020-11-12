from django.contrib import admin
from django.urls import path

from products.views import (product_details_view,
                            product_details_view_api,
                            products_list_view,
                            product_search_view,
                            product_add_view,
                            home_view)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name="home_view"),

    path('products/add/', product_add_view,
         name="product_add_view"),

    path('products/<int:productId>/', product_details_view,
         name="product_details_view"),

    path('products/', products_list_view,
         name="products_list_view"),

    path('products/search/', product_search_view, name="product_search_view"),

    path('api/products/<int:productId>/',
         product_details_view_api, name="product_details_view_api"),
]
