from django.contrib import admin
from .models import Question, Account, user_infor, avatar, questionType, answer, category


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('question type', {'fields': ['question_type']}),
        ('question category', {'fields': ['category']}),
        ('Date information and rate', {'fields': ['pub_date','rate'], 'classes': ['collapse']}),
        ('choices', {'fields': ['answer1', 'answer2', 'answer3', 'answer4']}),
        ('answer', {'fields': ['answer']})
    ]
    list_display = ('question_text', 'pub_date','rate')
    list_filter = ['pub_date','rate']
    search_fields = ['question_text']
    ordering = ['rate']
# class intire_information(admin.ModelAdmin):
# fieldsets = [
#      (None,{'fields':['rank']}),
#     ('user_information',{'fields':['score']}),
#     ('user profile',{'fields':['user']})
# ]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Account)
admin.site.register(user_infor)
admin.site.register(avatar)
admin.site.register(questionType)
admin.site.register(answer)
admin.site.register(category)
