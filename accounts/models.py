from django.contrib.auth.models import AbstractUser

# カスタムユーザーモデル
class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'
