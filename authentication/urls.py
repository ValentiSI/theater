from django.urls import include, path
from . import views


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/register', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('accounts/profile/info/', views.profile_info, name='profile_info'),
    path('accounts/profile/orders/', views.profile_orders, name='profile_orders'),
    path('accounts/profile/orders/order/<int:order_id>/', views.profile_order_details, name='profile_order_details')
]
