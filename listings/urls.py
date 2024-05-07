from django.urls import path
from listings import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all_listings/', views.listings, name='listing'),
    path('new_listing/', views.new, name='new_list'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('mylisting/', views.mylist, name = 'mylist'),
    path('edit_list/<int:pk>/', views.editList, name = 'edit_list'),
    path('delete/<int:pk>/', views.deleteList, name = 'delete'),
]