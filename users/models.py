from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserManager(BaseUserManager):
    # 유저를 생성하는 함수
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        if not username:
            raise ValueError('Users must have an email address')


        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True # 슈퍼 유저는 관리자 권한이 있음
        user.save(using=self._db)
        return user


class User(AbstractUser):
    # 메타 클래스는, DB 정보들에 대한 정보를 입력하는 곳
    class Meta:
        db_table = "usermodel"

    email = models.EmailField(verbose_name='이메일', max_length=255, unique=True)
    username = models.CharField("글 작성자", null=True, blank=True, max_length=50)
    year_of_birth = models.PositiveIntegerField("출생년도", null=True, blank=True)
    joined_at = models.DateField("계정 생성일", auto_now_add=True)
    is_active = models.BooleanField("활성화 여부", default=True)
    is_admin = models.BooleanField("관리자 여부", default=False)


    objects = UserManager() #쿼리셋 매니저가 UserManager임을 밝힘
    # USERNAME_FIELD 와 REQUIRED_FIELDS는 유저를 생성할 때, 필요한 필드이기 때문에 create_user 및 create_superuser시 필드를 추가시켜 줘야 함
    USERNAME_FIELD = 'email' # 회원가입시, 계정이름으로 가입하기 때문에, Unique=True 로 해주어야 하는 필드
    REQUIRED_FIELDS = ['username',]


    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
