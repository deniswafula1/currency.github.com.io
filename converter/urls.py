from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.home, name='home'),
    path('multi_result/', views.multi_result, name='multi_result'),
    path('add_favorites/', views.favorites, name='favorites'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('convert/', views.convert_currency, name='convert_currency'),
    path('favorites/', views.favorites_page, name='favorites_page'),
    path('historical_rates/', views.historical_rates, name='historical_rates'),
    path('historical_rates/<str:currency_code>/', views.historical_rates, name='historical_rates'),
    path('currency-register/', views.currency_register, name='currency_register'),
    path('logout/', views.user_logout, name='logout'),
    path('multi_result/', views.multi_result, name='multi_result'),
    #path('edit_favorite/<int:favorite_id>/', views.edit_favorite, name='edit_favorite'),
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('delete_favorite/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),

]
