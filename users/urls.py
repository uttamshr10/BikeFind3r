from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('log_out/', views.log_out, name='log_out'),
    path('register/', views.register, name = 'register'),
]