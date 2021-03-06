"""YCSGAME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import mainapp.views
from friendapp.views import send_friend_request, accept_friend_request

urlpatterns = [
    path('main/',include('mainapp.urls')),
    path('admin/', admin.site.urls),
    path('account/',include('accountapp.urls')),
    path('profile/',include('profileapp.urls')),
    path('friend/',include('friendapp.urls')),
    path('send_friend_request/<int:user_id>/', send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:request_id>/', accept_friend_request, name='accept friend request'),
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
