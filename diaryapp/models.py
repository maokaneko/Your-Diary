from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    # verbose_nameはモデルやモデルフィールドの名前を任意に変更できる
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True)
    # 画像
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    # 日付
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


    # モデル名を変更する(verbose_name_plural)
    class Meta:
        verbose_name_plural ='Diary'

    def __str__(self):
        return self.title