from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club', views.club, name='club'),
    path('schedule', views.schedule, name='schedule'),
    path('result', views.result, name='result'),
    path('blog', views.blog, name='blog'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    path('contact', views.contact, name='contact')

    
    
    
]