from django.urls import path
from . import views

app_name='searchapp'
urlpatterns=[
   path('questions_upload',views.add_questions_view,name='questions_upload'),
   path('upload',views.add_questions,name='upload'),
   path('login',views.login_view,name='login'),
   path('logout',views.logout_view,name='logout'),
   path('mentor_view',views.mentor_view,name='mentor_view'),
   path('', views.student_view, name='student_view'),

]
