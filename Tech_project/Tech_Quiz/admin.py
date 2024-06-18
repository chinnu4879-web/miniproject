from django.contrib import admin
from .models import Question, Option, Answer

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline, AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Answer)