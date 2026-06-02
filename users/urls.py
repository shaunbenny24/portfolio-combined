from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/token/', views.TokenObtainView.as_view(), name='token'),
]