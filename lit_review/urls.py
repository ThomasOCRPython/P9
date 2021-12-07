from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

import authentification.views
import flux.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentification/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('home/', flux.views.home, name='home'),
    path('ticket/create/', flux.views.ticket, name='ticket_create'),
    path('flux/<int:ticket_id>/', flux.views.view_ticket, name='view_ticket'),
    path('<int:ticket_id>/review/create/', flux.views.review, name='review_create'),
    
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)