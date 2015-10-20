from django.shortcuts import render,get_object_or_404
from django.template import  RequestContext,loader
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Account
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#@login_required(login_url='/login')
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
def login(request):
    return render(request,'quizapp/login_form.html')


def submitlogin(request):
        username=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
                return HttpResponseRedirect(reverse('index'))
        else:
                return render(request,'quizapp/login_form.html',{'error_message':'your password is wrong or user not exist'})
def logout(request):
    logout(request)
    return HttpResponseRedirect(render('login'))