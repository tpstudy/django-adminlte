from django.shortcuts import render, redirect
from django.contrib.auth import login, views as auth_views, logout
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy  # 添加这行
from .forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.decorators import login_required
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

# Create your views here.

# Authentication
def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      send_registration_email(user.email)
      return redirect('accounts:login')
  else:
    form = RegistrationForm()
  
  return render(request, 'accounts/register.html', {'form': form})

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm
  success_url = reverse_lazy('accounts:password_reset_done')
  email_template_name = 'accounts/password_reset_email.html'
  subject_template_name = 'accounts/password_reset_subject.txt'

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm
  success_url = reverse_lazy('accounts:password_reset_complete')

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm
  success_url = reverse_lazy('accounts:password_change_done')

class UserPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
  template_name = 'accounts/password_change_done.html'

def user_logout_view(request):
  logout(request)
  messages.success(request, "您已成功退出登录。")
  return redirect('accounts:login')  # 或者重定向到您想要的页面

def lockscreen(request):
  context = {
    'parent': '',
    'segment': ''
  }
  return render(request, 'pages/examples/lockscreen.html', context)

def legacy_user_menu(request):
  context = {
    'parent': 'extra',
    'segment': 'legacy_user'
  }
  return render(request, 'pages/examples/legacy-user-menu.html', context)

def language_menu(request):
  context = {
    'parent': 'extra',
    'segment': 'legacy_menu'
  }
  return render(request, 'pages/examples/language-menu.html', context)

def send_registration_email(user_email):
    subject = "欢迎注册"
    message = "感谢您注册我们的网站！"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from django.urls import reverse_lazy

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/forgot-password.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:password_reset_done')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        return form

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    form_class = SetPasswordForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New password'})
        form.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm new password'})
        return form

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'




@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    print(f"Form fields: {form.fields}")  # 添加这行来调试
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def profile_show(request):
    return render(request, 'accounts/profile_show.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_show')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile_edit.html', {'form': form})
