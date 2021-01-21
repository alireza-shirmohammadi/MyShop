from django.urls import path
from django.conf.urls import url
from . import views

app_name='shop'
urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<slug:Category_slug>/',views.products_list,name='product_list_by_category'),
    path('<slug:Category_slug>/<slug:subcat_slug>/',views.products_list,name='product_list_by_subcat'),
    path('<slug:c_slug>/<slug:subcat_slug>/<slug:p_slug>/',views.product_detail,name='product_detail'),
]
