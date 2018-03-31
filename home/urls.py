from django.conf.urls import url

from . import views

app_name='home'

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^save_weather$', views.save_weather),
    url(r'^chat_query/$', views.chat_query),
    url(r'chat_admin/$',views.chat_admin),
    url(r'administrator/$',views.administrator),
    url(r'^$',views.index,name='index'),
    url(r'^organic_farming$',views.organic_farming,name='organic_farming'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^weather/$',views.weather,name='weather'),
    url(r'^ask_question/$',views.ask_question,name='ask'),
    url(r'^add_comment/(?P<ans_id>[0-9]+)/$',views.add_comment,name='add_comment'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$',views.CommentDelete.as_view(),name='comment-delete'),
    url(r'^post/$',views.post,name='post'),
    url(r'^singleblog/$',views.singleblog,name='singleblog'),
   url(r'^blog/$',views.blog,name='blog'),
   url(r'^dashboard/$',views.dashboard,name='dashboard'),
   url(r'^forecast/$',views.weather_forecast,name='weather_forecast'),
   url(r'^predict/$',views.predict,name='predict'),
]


