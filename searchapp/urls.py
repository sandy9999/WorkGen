from django.urls import path
from . import views

app_name='searchapp'
urlpatterns=[
   path('questions_upload',views.add_questions_view,name='questions_upload'),
   path('generated_documents', views.generated_documents_view, name='generated_documents'),
   path('download_docx', views.download_docx, name='download_docx'),
   path('upload',views.add_questions,name='upload'),
   path('login',views.login_view,name='login'),
   path('logout',views.logout_view,name='logout'),
   path('mentor_view',views.mentor_view,name='mentor_view'),
   path('', views.student_view, name='student_view'),
   path('get_chapters', views.get_chapters, name='get_chapters'),
   path('get_test_paper', views.get_test_paper, name='get_test_paper'),
   path('get_generic_paper', views.get_generic_paper, name='get_generic_paper'),
]
