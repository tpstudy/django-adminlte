from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    CustomPasswordResetView, 
    CustomPasswordResetDoneView, 
    CustomPasswordResetConfirmView, 
    CustomPasswordResetCompleteView,
    user_logout_view
)

app_name = 'accounts'

urlpatterns = [

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('profile/', views.profile_show, name='profile_show'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done"),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
