from django.conf.urls import url
from django.conf import settings
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# from quizapp.views import MyRegistrationView
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/question/$', views.getQuestion, name='getquestion'),
    url(r'^getquestionlist/(?P<category>[a-z]+)/$', views.get_question_list, name='getquestionlist'),
    url(r'^getleaderboard/$', views.get_leaderboard, name='getleaderboard'),
    url(r'^getuserinfor/$', views.get_user_info, name='getuserinfor'),
    url(r'^updateprofile', views.update_profile, name='updateprofile'),
    url(r'^updatequestionrate', views.update_profile, name='updatequestionrate'),
    url(r'^updatescore', views.update_score, name='updatedcore'),
    url(r'^profile', views.update_profile, name='profile'),
    url(r'^questionrate', views.update_question_rate, name='questionrate'),
    #url(r'^accounts/register/complete/$',TemplateView.as_view(template_name='quizapp/index.html'),name='registration_complete'),
    url(r'^accounts/logout/$',auth_views.logout,{'template_name': 'quizapp/index.html'},name='auth_logout'),
    # url(r'^register/$',
    # MyRegistrationView.as_view(),
    #  name='registration_register'),
]
