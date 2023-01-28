from django.urls import path
from .views import (get_product_by_category_id,
list_all_products,
login_info,
register,
)
urlpatterns=[
    path('',login_info,name='login'),
    path("register/",register,name='register'),
    path('products/all',list_all_products),
    path('products/get/id/<int:pk>',get_product_by_category_id)
]