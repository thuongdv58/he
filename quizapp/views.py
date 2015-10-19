from django.shortcuts import render,get_object_or_404
from django.template import  RequestContext,loader
# Create your views here.
from django.http import HttpResponse
from .models import Question

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