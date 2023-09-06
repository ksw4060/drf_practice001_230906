from django.db import models
from users.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_user")
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="게시글 제목")
    content = models.TextField(verbose_name="게시글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    def __str__(self):
            return str(self.title)
