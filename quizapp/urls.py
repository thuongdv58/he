from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/question/$',views.getQuestion,name='getquestion'),
    url(r'^getquestionlist/(?P<question_type>[a-z]+)/$',views.get_question_list,name='getquestionlist')
    ]