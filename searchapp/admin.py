from django.contrib import admin
from searchapp.models import *


# Register your models here.

class ChapterFilter(admin.ModelAdmin):
    list_display = ['chapter_name', 'subject']
    list_filter = ['chapter_name']
    search_fields = ['chapter_name']


class QuestionsFilter(admin.ModelAdmin):
    list_display = ['chapter', 'question_weightage', 'question_type', 'uploaded_by', 'text', 'source']
    list_filter = ['chapter', 'question_weightage', 'question_type', 'uploaded_by', 'source']
    search_fields = ['text']


admin.site.register(Mentor)
admin.site.register(Board)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(GeneratedCustomizedPaper)
admin.site.register(GeneratedTestAndGenericPaper)
admin.site.register(Questions, QuestionsFilter)
admin.site.register(SubjectSplit)
admin.site.register(Chapter, ChapterFilter)
admin.site.register(FormAuth)
