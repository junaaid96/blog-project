from django.urls import path
from authors.views import registration, user_login, profile, edit_profile, user_logout, password_change

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/edit/password_change/', password_change, name='password_change')
]
