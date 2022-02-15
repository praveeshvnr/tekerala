
from django.urls import re_path
from  .import views


urlpatterns = [
    re_path(r'^index$',views.index,name='index'),
    re_path(r'^student$',views.student,name='student'),
    re_path(r'^admins$',views.admins,name='admin'),
    re_path(r'^adminpage$',views.adminpage,name='adminpage'),
    re_path(r'^studentview$',views.studentview,name='studentview'),
    re_path(r'^settings$',views.settings,name='settings'),
    re_path(r'^alog$',views.alog,name='alog'),
    re_path(r'^loginadmin$',views.loginadmin,name='loginadmin'),
    re_path(r'^save$',views.save,name='save'),
    re_path(r'^message$',views.message,name='message'),
    re_path(r'^delete/(?P<id>\d+)$',views.delete,name='delete'),
    re_path(r'^deletet/(?P<id>\d+)$',views.deletet,name='deletet'),
    re_path(r'^login$',views.login,name='login'),
    re_path(r'^loginn/(?P<id>\d+)$',views.loginn,name='login'),
    re_path(r'^edit/(?P<id>\d+)$',views.edit,name='edit'),
    re_path(r'^addadmin$',views.addadmin,name='addadmin'),
    re_path(r'^update/(?P<id>\d+)$',views.update,name='update'),
]
 
    