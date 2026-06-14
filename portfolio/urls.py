from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('resume/download/', views.download_resume, name='download_resume'),
    path('test-email/', views.test_email, name='test_email'),
]

