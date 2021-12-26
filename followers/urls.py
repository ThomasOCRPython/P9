from django.urls import path 
from . import views


urlpatterns = [
    path('user_follow/', views.user_follow, name='user_follow'),
    path('<int:followed_user_id>/delete', views.delete_user_follows, name='delete_user_follow'),

    
]




