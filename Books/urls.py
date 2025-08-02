from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),  # ⬅ renamed
    path('signup/', views.signup, name='register'),  # ⬅ register is the form name
    path('product/<int:id>/', views.product_details, name='product_details'),
]
