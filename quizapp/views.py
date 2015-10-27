from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,get_object_or_404
from django.template import  RequestContext,loader
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Account
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from django.core import serializers
from registration.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#@login_required(login_url='/login')
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


def get_question_list(request,question_type):
    questionlist=[]
    try:
        question_list= Question.objects.filter(question_type=question_type)[:10]
        for i in range(1,10):
            question={}
            question['id']=i
            question['content']=question_list[i-1].question_text
            question['options']=[question_list[i-1].answer1,question_list[i-1].answer2,question_list[i-1].answer3,question_list[i-1].answer4]
            if(question_list[i-1]=='A'):
                question['answer']=0
            elif(question_list[i-1]=='B'):
                question['answer']=1
            elif(question_list[i-1]=='C'):
                question['answer']=2
            elif(question_list[i-1]=='D'):
                question['answer']=3
            questionlist.append(question)
        return JsonResponse(questionlist)
    except ObjectDoesNotExist:
        return JsonResponse({'error_message':'not exist this type of question!'})
def update_score(request,score):
    raise NotImplementedError
def update_profile(request):
    raise NotImplementedError
