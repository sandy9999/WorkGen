from django.urls import path
from . import views

app_name='searchapp'
urlpatterns=[
   path('',views.upload_view,name='upload'),
  path('upload',views.add_questions,name='add_questions'),
   
]


