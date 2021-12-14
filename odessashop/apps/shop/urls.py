from django.urls import path
from .views import *


urlpatterns = [
    path('category-list/', CategoryListAPI.as_view(), name=''),
    path('card-get/<int:pk>', CardGetAPI.as_view(), name=''),
    path('card-create/', CardCreateAPI.as_view(), name=''),
    path('card-delete/<int:pk>', CardDeleteAPI.as_view(), name=''),
    path('card-partial-update/<int:pk>', CardPartialUpdateAPI.as_view(), name=''),
    path('shop-create/', ShopCreateAPI.as_view(), name=''),
    path('shop-delete/<int:pk>', ShopDeleteAPI.as_view(), name=''),
    path('shop-get/<int:pk>', ShopGetAPI.as_view(), name=''),
    path('shop-get-by-category/<int:pk>', ShopsGetByCategory.as_view(), name=''),
    path('shop-get-by-username/<str:username>', ShopsGetByUsername.as_view(), name=''),
    path('shop-partial-update/<int:pk>', ShopPartialUpdateAPI.as_view(), name=''),
]
