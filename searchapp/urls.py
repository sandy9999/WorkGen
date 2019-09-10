from django.urls import path
from . import views

app_name = 'searchapp'
urlpatterns = [
    path('questions_upload', views.add_questions_view, name='questions_upload'),
    path('generated_documents', views.generated_documents_view, name='generated_documents'),
    path('download_customized_docx', views.download_customized_docx, name='download_customized_docx'),
    path('download_test_and_generic_docx', views.download_test_and_generic_docx, name='download_test_and_generic_docx'),
    path('upload', views.add_questions, name='upload'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('mentor_view', views.mentor_view, name='mentor_view'),
    path('student_view', views.student_view, name='student_view'),
    path('chapter_and_split_view', views.chapter_and_split_view, name='chapter_and_split_view'),
    path('get_chapters', views.get_chapters, name='get_chapters'),
    path('add_chapter', views.add_chapter, name='add_chapter'),
    path('delete_chapters', views.delete_chapters, name='delete_chapters'),
    path('display_split_table', views.display_split_table, name='display_split_table'),
    path('delete_subject_split', views.delete_subject_split, name='delete_subject_split'),
    path('get_grades', views.get_grades, name='get_grades'),
    path('get_subjects', views.get_subjects, name='get_subjects'),
    path('add_subject_split', views.add_subject_split, name='add_subject_split'),
    path('get_test_paper', views.get_test_paper, name='get_test_paper'),
    path('get_generic_paper', views.get_generic_paper, name='get_generic_paper'),
    path('get_customize_paper', views.get_customize_paper, name='get_customize_paper'),
    path('generate_optional_inputs', views.generate_optional_inputs, name='generate_optional_inputs'),
    path('', views.home, name='home'),
    path('contact', views.contact),
    path('get_dummy_tracker', views.get_dummy_tracker),
]
