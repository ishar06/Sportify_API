from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('exchange-policy/', views.exchange_policy, name='exchange_policy'),
]