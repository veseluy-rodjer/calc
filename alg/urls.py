from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.head, name='head'),
    url(r'^process/$', views.process, name='process'),
    url(r'^addd/$', views.addd, name='addd'),
    url(r'^begin/$', views.begin, name='begin'),
    url(r'^end/$', views.end, name='end'),
    url(r'^start_alg/$', views.start_alg, name='start_alg'),
    url(r'^process1/$', views.process1, name='process1'),
]

