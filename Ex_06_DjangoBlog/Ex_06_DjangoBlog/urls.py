"""Ex_06_DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from endusers import views as enduser_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', enduser_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='endusers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'endusers/logout.html'), name='logout'),
    path('profile/', enduser_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'endusers/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'endusers/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name= 'endusers/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'endusers/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('fruitfulblog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
