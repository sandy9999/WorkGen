from django.urls import path

from . import views

urlpatterns = [
    path('',views.student_view,name="student_view"),
    path('download_customized/',views.download_customized,name="download_customized"),
    path('download_test/',views.download_test,name="download_test"),
    path('download_generic_random/',views.download_generic_random,name="download_generic_random"),
    path('download_generic_segregated/',views.download_generic_segregated,name="download_generic_segregated"),
    
]
