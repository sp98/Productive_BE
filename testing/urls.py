from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as token_view

urlpatterns = [
    url(r'^user-check/$', views.validateUserName.as_view(), name='validate_username'),
    url(r'^users/$', views.ListUsers.as_view(), name='users'),
    url(r'^login/', views.loginUser.as_view(), name='login'),
    url(r'^logout/', views.logoutUser.as_view(), name='logout'),
    url(r'^sign_up/$', views.SignUpUsers.as_view(), name='sign_up'),
    url(r'^user/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyUsers.as_view(), name='user_detail'),
    url(r'^(?P<user_id>\d+)/daily/$', views.ListCreateDailyTasks.as_view(), name='daily_tasks'),
    url(r'^(?P<user_id>\d+)/daily/(?P<pk>\d+)$', views.RetrieveUpdateDestroyDailyTasks.as_view(), name='daily_task_detail'),

]
