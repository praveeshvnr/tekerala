"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('student/',views.student),
    path('admins/',views.admins),
    path('adminpage/',views.adminpage),
    path('studentview/',views.studentview),
    path('settings/',views.settings),
    path('alog/',views.alog),
    path('loginadmin/',views.loginadmin),
    path('save/',views.save),
    path('message/',views.message),
    path('delete/<int:id>',views.delete),
    path('deletet/<int:id>',views.deletet),
    path('login/',views.login),
    path('loginn/<int:id>',views.loginn),
    path('edit/<int:id>',views.edit),
    path('addadmin/',views.addadmin),
    path('update/<int:id>',views.update),
]
