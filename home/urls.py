from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^save_weather$', views.save_weather),
    url(r'^chat_query/$', views.chat_query),

]
