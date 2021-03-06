from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('en/', views.viewEN, name='en'),
    path('ar/', views.viewAR, name='ar'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.homepage, name='homepage'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
