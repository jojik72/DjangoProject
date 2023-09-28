from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]