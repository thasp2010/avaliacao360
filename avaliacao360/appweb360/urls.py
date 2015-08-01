from django.conf.urls import patterns, include, url

urlpatterns = patterns('appweb360.views',
    url(r'^$','appweb_home', name='appweb_home'),
    url(r'^home/$', 'home', name='url_home'),
    url(r'^home/(?P<id>\d+)$','questionario',name='url_questionario'),
    url(r'^home/salvar/$','salvarQuestionario'),
    url(r'^home/some_view/$','lista_resposta',name= 'url_relatorio'),
    url(r'^home/logout/$', 'logout', name='url_logout'),

)