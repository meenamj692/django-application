from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_default'),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    #url(r'^detail/(?P<course_title>[a-zA-Z ]+)/', views.detail, name='detail'),
    url(r'^detail/(?P<course_num>[0-9]+)/', views.detail, name='detail'),
    url(r'^topics/$',views.topics, name='topics'),
    url(r'^addtopic/$', views.addtopic, name='addtopic'),
    url(r'^topics/(?P<topic_id>\d+)/',views.topicdetail, name='topicdetail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$',views.user_logout, name='logout'),
    url(r'^mycourses/$', views.mycourses, name='mycourses'),
    url(r'^forgotpass/$',views.forgotpass, name='forgotpass')
    ]