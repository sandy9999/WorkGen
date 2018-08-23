from django.contrib import admin
from searchapp.models import Mentor, Subject, GeneratedQuestionPaper
# Register your models here.

admin.site.register(Mentor)
admin.site.register(Subject)
admin.site.register(GeneratedQuestionPaper)