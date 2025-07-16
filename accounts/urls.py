from django.urls import path
from . import views
from .views import customer_login_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('get-cities/', views.get_cities, name='get_cities'),
    path('info/', views.account_info, name='accountInfo'),
    path('profile/', views.user_profile_view, name='user_profile'),
    path('login/', customer_login_view, name='login'),
    path('signup/user/', views.signup_userInfo_view, name='signup-userInfo'),
    path('signup/contact/', views.signup_contactInfo_view, name='signup-contactInfo'),
    path('signup/contact/ajax/get-cities/', views.get_cities, name='get_cities'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]
