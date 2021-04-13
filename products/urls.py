from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_product_view,name='create'),
    path('<slug>/', views.detail_product_view, name='details'),
    path('<slug>/edit/', views.edit_product_view, name='edit'),
    path('<slug>/delete/', views.delete_product_view, name='delete'),
    path('upvote/',views.upvote_view,name="upvote")
]