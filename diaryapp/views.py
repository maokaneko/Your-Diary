from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import InquiryForm

# IndexView
class DiaryIndexView(TemplateView):
    template_name = 'diary/index.html'


# DiaryInquiryView
class DiaryInquiryView(FormView):
    template_name = 'diary/inquiry.html'
    #formの設定(form_class)
    form_class = InquiryForm
