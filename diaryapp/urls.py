from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.DiaryIndexView.as_view(), name='diary_index'),
    path('inquiry/', views.DiaryInquiryView.as_view(), name='diary_inquiry'),
]
