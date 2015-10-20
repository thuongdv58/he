from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login, name='login'),
    url(r'^submit/$',views.submitlogin,name='submitlogin'),
    url(r'^(?P<question_id>[0-9]+)/question/$',views.getQuestion,name='getquestion')
]