from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.IndexView.as_view(), name='diary_index'),
]
