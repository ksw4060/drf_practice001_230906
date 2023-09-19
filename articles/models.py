from django.db import models
from users.models import User
from uuid import uuid4
from datetime import date
import os
from django.urls import reverse




# 이미지 파일 이름 uuid형식으로 바꾸기
def rename_imagefile_to_uuid(instance, filename):
    now = date.today()
    upload_to = f"media/img/{now.year}/{now.month}/{now.day}/{instance}"
    ext = filename.split(".")[-1]
    uuid = uuid4().hex

    if instance:
        filename = "{}_{}.{}".format(uuid, instance, ext)
    else:
        filename = "{}.{}".format(uuid, ext)
    return os.path.join(upload_to, filename)


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_user")
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name="게시글 제목")
    content = models.TextField(verbose_name="게시글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")
    # 이미지
    uploaded_image = models.ImageField(
        upload_to=rename_imagefile_to_uuid, verbose_name="업로드이미지", blank=True, null=True
    )
    def __str__(self):
            return str(self.title)

    def get_absolute_url(self):
        return reverse('article_detail_view', kwargs={"article_id":self.pk}) # 까묵지 말제이~~??
