from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^save_weather$', views.save_weather),
    url(r'^chat_query/$', views.chat_query),
    url(r'chat_admin/$',views.chat_admin),
    url(r'administrator/$',views.administrator)
]
