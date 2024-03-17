from django.urls import path
from django.views.generic import ListView, DetailView
from .models import News
from . import views

urlpatterns = [
    path(
        '',
        ListView.as_view(queryset=News.objects.all().order_by("-date"),
                         template_name="mainApp/news.html")
    ),
    path(
        'news/<int:pk>',
        DetailView.as_view(model=News, template_name="mainApp/post.html")
    ),
    path('contacts/', views.contacts, name='contacts'),
    path('about-us/', views.about, name='about'),
]
