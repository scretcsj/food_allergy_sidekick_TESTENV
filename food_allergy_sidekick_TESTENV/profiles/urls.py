from django.urls import path
from .views import signup, view_profile, edit_profile, home, logout_user, login_user
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
