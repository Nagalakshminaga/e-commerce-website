from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login_usage',views.login_usage,name='login_usage'),
    path('logout_page',views.logout_page,name='logout_page'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
]