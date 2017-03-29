from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.erudition_add, name='erudition_add'),
    url(r'^start_erudition/$', views.start_erudition, name='start_erudition'),
    url(r'^process1/$', views.erudition_process1, name='erudition_process1'),
    url(r'^process/$', views.erudition_process, name='erudition_process'),
    url(r'^end/$', views.erudition_end, name='erudition_end'),
    url(r'^result/$', views.erudition_result, name='erudition_result'),
]