from django.urls import path

from . import views

urlpatterns = [
    path("", views.ToppageView.as_view(), name='top_page'),
]
