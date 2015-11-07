from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,get_object_or_404, render_to_response
from django.template import  RequestContext,loader
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Account,user_infor,avatar
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from django.core import serializers
from registration.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quizapp.forms import ScoreUpdate,ProfileForm


class RegistrationViews(RegistrationView):

    def get_success_url(request, new_user):
        return  reverse('registration_complete')

    def register(self, request, form):
        """
        Implement user-registration logic here. Access to both the
        request and the full cleaned_data of the registration form is
        available here.
        """
        raise NotImplementedError


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('quizapp/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


def getQuestion(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'quizapp/question.html',{'question':question})


@login_required(login_url='/login')
def get_question_list(request,category):
    try:

        #lists=Question.objects.all()
        #questionlist =serializers.serialize('json',lists)               ///get question in default form
        #return JsonResponse(questionlist,safe=False)

        #return HttpResponse(serializers.serialize('json', Question.objects.all()))

        questionlist=[]
        lists=\
            Question.objects.filter(category__category__icontains=category)[:10]
        for quest in lists:
            question={}
            question['id']=quest.pk
            question['content']=quest.question_text
            a=quest.answer1
            b=quest.answer2
            c=quest.answer3
            d=quest.answer4
            question['options']=[a,b,c,d]
            q=quest.answer
            temp=q.answer
            if(temp=='A'):
                answer=0
            elif(temp=="B"):
                answer=1
            elif(temp=='C'):
                answer=2
            else:
                answer=3
            type=quest.question_type
            questiontype=type.type
            question['type']=questiontype
            question['answer']= answer
            questionlist.append(question)
        return JsonResponse(questionlist,safe=False)
    except ObjectDoesNotExist:
        raise Exception('question type not match any in the database!')


@login_required(login_url='/login')
def get_user_info(request):
    try:
        user=user_infor.objects.get(user=request.user)
        response={}
        tem=user.user
        response['firstname']=tem.first_name
        response['lastname']=tem.last_name
        tem=user.avatar
        response['avatar']=tem.avatar
        return JsonResponse(response)
    except:
        user=user_infor.objects.create(user=request.user)
        response={}
        tem=user.user
        response['firstname']=tem.first_name
        response['lastname']=tem.last_name
        tem=user.avatar
        response['avatar']=tem.avatar
        return JsonResponse(response)


@login_required(login_url='/login')
def get_leaderboard(request):
    userlist=[]
    lists= \
        user_infor.objects.all().order_by('-score')[:10]
    for user in lists:
        doc={}
        temp=user.user
        u=temp.username
        doc['name']=u
        doc['score']=user.score
        temp=user.avatar
        u=temp.avatar
        doc['avatar']=u
        userlist.append(doc)
    return JsonResponse(userlist,safe=False)


@login_required(login_url='/login')
def update_score(request):
   try:
        user=user_infor.objects.get(user=request.user)

        if request.POST:
             user.score=user.score+int(str(request.POST['score']))
             user.save()
             return  HttpResponse({},content_type="application/json")
        else:
            form=ScoreUpdate()
            variables = RequestContext(request, {
            'form': form
            })
            return render_to_response('quizapp/post.html', variables)
   except ObjectDoesNotExist:
        raise Exception('user does not exist!')


@login_required(login_url='/login')
def update_profile(request):
    if request.method == 'POST':
        UserInfor = user_infor.objects.filter(user=request.user).count()
        if UserInfor==0:
            user_infor.objects.create(user=request.user)
        UserInfor=user_infor.objects.get(user=request.user)
        user=request.user
        user.first_name=request.POST['firstname']
        user.last_name=request.POST['lastname']
        ava=avatar.objects.filter(avatar=request.POST['avatar'])
        UserInfor.avatar=ava[0]
        user.save()
        UserInfor.save()
        return HttpResponse({},content_type='application/json')
    else:
            form=ProfileForm()
            variables = RequestContext(request, {
            'form': form
            })
            return render_to_response('quizapp/profile.html', variables)


@login_required(login_url='/login')
def update_question_rate(request):
    if request.method=='POST':
        questionlist=request.POST['votelist']
        for quest in questionlist:
            question=Question.objects.get(pk=int(quest))
            question.rate=question.rate+1
        return HttpResponse({'success':'ok'},content_type='application/json')
    else:
        raise Exception('f*** you! just post not get ok!')

from django.conf import settings
from django.utils.module_loading import import_string
#REGISTRATION_FORM_PATH = getattr(settings, 'REGISTRATION_FORM',
#                                 'quizapp.forms.MyRegistrationForm')
#REGISTRATION_FORM = import_string(REGISTRATION_FORM_PATH)
#from registration.views import RegistrationView
#class MyRegistrationView(RegistrationView):
#    form_class = REGISTRATION_FORM
#    x=0

