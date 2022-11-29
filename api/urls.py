from knox import views as knox_views
from django.urls import path
from . import views

urlpatterns = [
    path('api/account/get-all', views.getaccount),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('product/get-all', views.getproduct),
    path('product/add-product', views.addproduct),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
