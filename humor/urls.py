from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^start_humor/$', views.start_humor, name='start_humor'),
    url(r'^start_process/$', views.start_process, name='start_process'),
    url(r'^process/(?P<v>[0-9]+)/$', views.humor_process, name='humor_process'),
    url(r'^result/$', views.humor_result, name='humor_result'),
    url(r'^add/$', views.humor_add, name='humor_add'),    
]