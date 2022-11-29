from knox import views as knox_views
from django.urls import path
from . import views

urlpatterns = [
    # account
    path('api/account/get-all', views.getaccount),
    path('api/account/edit/<int:id>', views.update_account, name='update_account'),
    path('api/account/delete/<int:id>',
         views.delete_account, name='delete_account'),
    # product
    path('api/product/get-all', views.getproduct),
    path('api/product/add-product', views.add_product),
    path('api/product/edit/<int:id>', views.edit_product),
    path('api/product/delete/<int:id>', views.delete_product),
    # requestForm
    path('api/request-form/get-all', views.getRequestForm),
    path('api/request-form/add', views.addrequest),
    path('api/request-form/change-state/<int:id>',
         views.change_state, name='change-state'),

    # user
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
