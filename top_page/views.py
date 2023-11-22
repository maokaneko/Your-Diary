from django.shortcuts import render
from django.views.generic import TemplateView


class ToppageView(TemplateView):
  template_name = 'top_page.html'
