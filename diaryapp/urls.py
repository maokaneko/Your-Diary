from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.DiaryIndexView.as_view(), name='diary_index'),
    path('inquiry/', views.DiaryInquiryView.as_view(), name='diary_inquiry'),
    path('list/', views.DiaryListView.as_view(), name='diary_list'),
    path('create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('update/<int:pk>/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('delete/<int:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),
]
