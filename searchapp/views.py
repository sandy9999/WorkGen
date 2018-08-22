from django.shortcuts import render
import logging
from .models import Mentor,Questions,MCQOptions
# Create your views here.

logger = logging.getLogger(__name__)

def student_view(request):
    subject = Questions.objects.order_by('subject').values('subject').distinct()
    chap = Questions.objects.filter(subject='Science')
    template_data = {'subject':subject,'chap':chap}
    return render(request,'student_view.html',template_data)
