from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('account/', include('django.contrib.auth.urls')),
    
    path('account/register/',views.register, name='register'),
    path("account/edit/", views.edit, name='edit'),
]
