from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import InquiryForm, DiaryCreateForm
from .models import Diary



# UserPassesTestMixin(ログイン済みユーザーのアクセスを制限する機能を提供している)
class OnlyYourMinxin(UserPassesTestMixin):
    raise_exception =True

    # test_funcメソッド(真偽判定)
    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        diary = get_object_or_404(Diary, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == diary.user




# IndexView
class DiaryIndexView(TemplateView):
    template_name = 'diary/index.html'


# DiaryInquiryView
class DiaryInquiryView(FormView):
    template_name = 'diary/inquiry.html'
    #formの設定(form_class)
    form_class = InquiryForm


# DiaryListView
class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/list.html'
    paginate_by = 3

    # ログインユーザーに紐づいたデータを表示する(get_queryset)
    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


# DiaryDetailView
class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = Diary
    template_name = 'diary/detail.html'



# DiaryCreateView
class DiaryCreateView(LoginRequiredMixin, CreateView):
    model = Diary
    template_name = 'diary/create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary_list')

    # form_validメソッド:フォームのバリデーションに問題が無ければ実行されるメソッド
    def form_valid(self, form):
        # form.saveメソッド:フォームの内容をデータベースに保存する
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, "日記を作成しました。")
        return super().form_valid(form)

    # form_invalid(フォームバリデーションが失敗した時に実行される)
    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)




# DiaryUpdateView
class DiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    template_name = 'diary/update.html'
    form_class = DiaryCreateForm

    # get_success_url():URLが動的に変化するページに遷移させるときに使用する
    def get_success_url(self):
        return reverse_lazy('diary_detail', kwargs={'pk':self.kwargs['pk']})

    # form_validメソッド:フォームのバリデーションに問題が無ければ実行されるメソッド
    def form_valid(self, form):
        messages.success(self.request, "日記を更新しました。")
        return super().form_valid(form)

    # form_invalid(フォームバリデーションが失敗した時に実行される)
    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)




# DiaryDeleteView
class DiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    template_name = 'diary/delete.html'
    success_url = reverse_lazy('diary_list')

    # deleteメソッド(DeleteViewの削除成功時に実行されるメソッド)
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)