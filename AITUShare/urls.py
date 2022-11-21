"""AITUShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from profiles.views import profile, index
from forum.views import forum_index, forum_person, forum_create_topic

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^profile/*$', index, name='profile_index'),
    path('profile/<str:profile_login>', profile, name="profile_personal"),

    re_path('^login', views.login_page, name="login_page"),
    re_path('^register', views.register_page, name="register_page"),
    re_path(r'^logout', views.logout, name="logout"),
    re_path(r'^verify_auth', views.verify_auth),

    re_path(r'^forum/*$', forum_index, name="forum_index"),
    re_path(r'^forum/create_topic/*$', forum_create_topic, name="create_topic"),
    path('forum/<int:topic_id>', forum_person),

    re_path('admin/*', admin.site.urls)
]

