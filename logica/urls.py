from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^start_logica/$', views.start_logica, name='start_logica'),
    url(r'^begin/$', views.logica_begin, name='logica_begin'),
    url(r'^end/$', views.logica_end, name='logica_end'),
    url(r'^process1/$', views.logica_process1, name='logica_process1'),
    url(r'^process/$', views.logica_process, name='logica_process'),
    url(r'^add/$', views.logica_add, name='logica_add'),
]

