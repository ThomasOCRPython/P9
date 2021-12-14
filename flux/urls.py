
from django.urls import path 
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('ticket/create/', views.ticket, name='ticket_create'),
    path('<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    path('<int:ticket_id>/review/create/', views.review, name='review_create'),
]