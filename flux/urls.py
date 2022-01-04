from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("ticket/create/", views.ticket, name="ticket_create"),
    path(
        "ticket_and_review/create/",
        views.ticket_and_review,
        name="ticket_and_review_create",
    ),
    path("<int:ticket_id>/", views.view_ticket, name="view_ticket"),
    path("<int:ticket_id>/edit_ticket/", views.edit_ticket, name="edit_ticket"),
    path("<int:ticket_id>/delete_ticket/", views.delete_ticket, name="delete_ticket"),
    path("<int:review_id>/edit_review/", views.edit_review, name="edit_review"),
    path("<int:review_id>/delete_review/", views.delete_review, name="delete_review"),
    path("<int:ticket_id>/review/create/", views.review, name="review_create"),
    path("posts/", views.posts, name="posts"),
]
