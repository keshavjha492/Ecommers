from django.contrib import admin
from django.urls import path, include


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import userlogin, UserProfileView, ProductListView, ProductDetailView, OrderCreateView, OrderHistoryView, CartView, RegisterView

urlpatterns = [
    path('api/userlogin/', userlogin.as_view(), name='userlogin'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/profile/', UserProfileView.as_view()),
    path('api/products/', ProductListView.as_view()),
    path('api/products/<pk>/', ProductDetailView.as_view()),
    path('api/orders/', OrderCreateView.as_view()),
    path('api/orders/history/', OrderHistoryView.as_view()),
    path('api/cart/', CartView.as_view()),
]