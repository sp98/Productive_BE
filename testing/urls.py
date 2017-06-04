from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.ListCreateUsers.as_view(), name='users'),
    url(r'^user/create/$', views.CreateUser.as_view(), name='create_users'),
    url(r'^user/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyUsers.as_view(), name='user_detail'),
    url(r'^(?P<user_id>\d+)/daily/$', views.ListCreateDailyTasks.as_view(), name='daily_tasks'),
    url(r'^(?P<user_id>\d+)/daily/(?P<pk>\d+)$', views.RetrieveUpdateDestroyDailyTasks.as_view(), name='daily_task_detail'),

]
