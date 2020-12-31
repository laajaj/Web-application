"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path,re_path
from django.contrib.auth.views import LoginView

from django.urls import include
# import wwwApp.views.WebServices
from wwwApp.views import views

from django.contrib import admin


urlpatterns = [

    path('search/', views.search_by_destination, name='search'),
    path('admin/', admin.site.urls, name='admin_page'),
    path('buy_ticket', views.buy_ticket),
    url(r'^logout/$', views.logout_view, name='logout'),

    path('login_page/', auth_views.LoginView.as_view(template_name='wwwApp/login_page.html'), name='login_page'),
    url(r'^signup/$', views.signup, name='signup'),
    path('flights/<int:id>', views.flight_details, name='flight_details'),
    re_path('', views.home),
    url(r'^home/.*', views.home, name='home'),

]

