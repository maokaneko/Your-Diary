from django.shortcuts import render
from django.views.generic import TemplateView


# IndexView
class IndexView(TemplateView):
    template_name = 'diary/index.html'
