from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    score=models.IntegerField(blank=False,default=0)
    rank=models.IntegerField(blank=False,default=0)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email
class avatar(models.Model):
    avatar=models.TextField(max_length=50)
    user=models.ManyToManyField(User)
    def __unicode__(self):
        return self.avatar
class user_infor(models.Model):
    user=models.OneToOneField(User,primary_key=True)
    score=models.IntegerField(default=0)
    rank=models.IntegerField(default=0)
    def __unicode__(self):
        return '{0},{1}'.format(self.rank,self.score)
class questionType(models.Model):
    type=models.TextField(max_length=50)
    def __unicode__(self):
        return self.type
class answer(models.Model):
    answer=models.CharField(max_length=1,default='A')
    def  __unicode__(self):
        return "{0}".format(self.answer)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_type = models.ForeignKey(questionType)
    answer1=models.TextField(max_length=200)
    answer2=models.TextField(max_length=200)
    answer3=models.TextField(max_length=200)
    answer4=models.TextField(max_length=200)
    answer=models.ForeignKey(answer)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text