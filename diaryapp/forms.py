from django import forms

from .models import Diary

# InquiryForm
class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # name
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前はここに入れてください。'

        #email
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスはここに入力ください。'

        #title
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        #message
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'




# DiaryCreateForm
class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)

    # インスタンスを生成した際に、1番最初に呼び出される関数
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 全フォームフィールドにBootstrapのform-controlクラスを追加する
            field.widget.attrs['class'] = 'form-control'
