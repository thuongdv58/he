from django.contrib import admin
from .models import Question, Account, user_infor, avatar, questionType, answer, category ,multi_answer,Choice,toggle_choice,single_answer


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('question type', {'fields': ['question_type']}),
        ('question category', {'fields': ['category']}),
        ('Date information and rate', {'fields': ['pub_date','rate'], 'classes': ['collapse']}),
        ('four-quarter', {'fields': ['answer'],'classes':['collapse']}),
        ('single-select',{'fields':['single_answer'],'classes':['collapse']}),
        ('single-select-item',{'fields':['single_answer'],'classes':['collapse']}),
        ('multi-select',{'fields':['multi_select_answer'],'classes':['collapse']}),
        ('true-false',{'fields':['true_false_choice'],'classes':['collapse']}),
        ('fill-blank',{'fields':['fill_blank_answer'],'classes':['collapse']}),
        ('picker',{'fields':['max','min','picker_answer'],'classes':['collapse']}),
        ('fill-two-blank',{'fields':['fill_two_blank1','fill_two_blank2'],'classes':['collapse']}),
    ]
    list_display = ('question_text', 'pub_date','rate')
    list_filter = ['pub_date','rate']
    search_fields = ['question_text']
    ordering = ['rate']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(user_infor)
admin.site.register(avatar)
admin.site.register(questionType)
admin.site.register(answer)
admin.site.register(category)
admin.site.register(single_answer)