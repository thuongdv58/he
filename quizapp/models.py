from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    score = models.IntegerField(blank=False, default=0)
    rank = models.IntegerField(blank=False, default=0)
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
    avatar = models.TextField(max_length=50)

    def __unicode__(self):
        return self.avatar


class user_infor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    avatar = models.ForeignKey(avatar, default=1)

    def __unicode__(self):
        return '{0},{1}'.format(self.rank, self.score)


class questionType(models.Model):
    type = models.TextField(max_length=50)

    def __unicode__(self):
        return self.type


class answer(models.Model):
    answer = models.CharField(max_length=1, default='A')

    def __unicode__(self):
        return "{0}".format(self.answer)


class single_answer(models.Model):
    answer = models.IntegerField(max_length=1, default=0)

    def __unicode__(self):
        return str(self.answer)


class multi_answer(models.Model):
    answer = models.IntegerField(default=0)

    def __unicode__(self):
        return "{0}".format(self.answer)


class category(models.Model):
    category = models.TextField(max_length=50, default="")

    def __unicode__(self):
        return self.category


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_type = models.ForeignKey(questionType)
    category = models.ForeignKey(category)
    rate = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    answer = models.ForeignKey(answer,default=1)
    single_answer = models.ForeignKey(single_answer, default=1)
    multi_select_answer = models.ManyToManyField(multi_answer,blank=True)
    true_false_choice = models.BooleanField(choices=((False, 'False'), (True, 'True')), default=True)
    fill_blank_answer = models.CharField(max_length=100, blank=True)
    max = models.IntegerField(default=0)
    min = models.IntegerField(default=0)
    picker_answer = models.IntegerField(default=0)
    fill_two_blank1 = models.CharField(max_length=50, blank=True)
    fill_two_blank2 = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.choice_text


class toggle_choice(models.Model):
    ob = models.CharField(max_length=30)
    answer = models.CharField(max_length=30)

    def __unicode__(self):
        return '{0},{1}'.format(self.ob, self.answer)
